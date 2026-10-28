
from typing import Optional
from decimal import Decimal

from fastapi import FastAPI, Depends, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models import Product, CartItem


app = FastAPI(title="ShapDrop")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_cart_id():
    return "guest"


def get_cart_count(db: Session):
    items = (
        db.query(CartItem)
        .filter(CartItem.cart_id == get_cart_id())
        .all()
    )
    return sum(item.quantity for item in items)


def get_cart_data(db: Session):
    cart_items = (
        db.query(CartItem)
        .filter(CartItem.cart_id == get_cart_id())
        .all()
    )

    items = []
    subtotal = Decimal("0.00")

    for item in cart_items:
        product = (
            db.query(Product)
            .filter(Product.id == item.product_id)
            .first()
        )

        if product is None or product.stock <= 0:
            db.delete(item)
            continue

        if item.quantity > product.stock:
            item.quantity = product.stock

        line_total = Decimal(str(product.price)) * item.quantity
        subtotal += line_total

        items.append({
            "product": product,
            "quantity": item.quantity,
            "line_total": line_total,
        })

    db.commit()

    return {
        "items": items,
        "subtotal": subtotal,
        "count": sum(item["quantity"] for item in items),
    }


@app.get("/", response_class=HTMLResponse)
def home_page(
    request: Request,
    db: Session = Depends(get_db),
):
    # Get distinct categories from MySQL
    categories = [
        row[0]
        for row in (
            db.query(Product.category)
            .filter(Product.category.isnot(None))
            .distinct()
            .order_by(Product.category)
            .all()
        )
        if row[0] and row[0].strip()
    ]

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "categories": categories,
            "cart_count": get_cart_count(db),
        },
    )


@app.get("/products", response_class=HTMLResponse)
def list_products(
    request: Request,
    q: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Product)

    if q and q.strip():
        query = query.filter(
            Product.name.ilike(f"%{q.strip()}%")
        )

    if category and category.strip():
        query = query.filter(
            Product.category == category.strip()
        )

    products = query.order_by(Product.id).all()

    categories = [
        row[0]
        for row in (
            db.query(Product.category)
            .filter(Product.category.isnot(None))
            .distinct()
            .order_by(Product.category)
            .all()
        )
        if row[0] and row[0].strip()
    ]

    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={
            "products": products,
            "categories": categories,
            "q": q or "",
            "selected": category or "",
            "cart_count": get_cart_count(db),
        },
    )


@app.get("/product/{product_id}", response_class=HTMLResponse)
def product_detail(
    request: Request,
    product_id: int,
    db: Session = Depends(get_db),
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return templates.TemplateResponse(
        request=request,
        name="product_detail.html",
        context={
            "product": product,
            "cart_count": get_cart_count(db),
        },
    )


@app.post("/cart/add/{product_id}")
def add_to_cart(
    product_id: int,
    quantity: int = Form(1),
    db: Session = Depends(get_db),
):
    if quantity < 1:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be at least 1",
        )

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    if product.stock <= 0:
        raise HTTPException(
            status_code=400,
            detail="Product is out of stock",
        )

    cart_item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == get_cart_id(),
            CartItem.product_id == product_id,
        )
        .first()
    )

    current_quantity = cart_item.quantity if cart_item else 0

    if current_quantity + quantity > product.stock:
        raise HTTPException(
            status_code=400,
            detail=f"Only {product.stock} units are available",
        )

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(
            cart_id=get_cart_id(),
            product_id=product_id,
            quantity=quantity,
        )
        db.add(cart_item)

    db.commit()

    return RedirectResponse("/cart", status_code=303)



@app.get("/cart", response_class=HTMLResponse)
def view_cart(
    request: Request,
    db: Session = Depends(get_db),
):
    data = get_cart_data(db)

    return templates.TemplateResponse(
        request=request,
        name="cart.html",
        context={
            **data,
            "cart_count": data["count"],
        },
    )


@app.post("/cart/update/{product_id}")
def update_cart(
    product_id: int,
    quantity: int = Form(...),
    db: Session = Depends(get_db),
):
    if quantity < 1:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be at least 1",
        )

    cart_item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == get_cart_id(),
            CartItem.product_id == product_id,
        )
        .first()
    )

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found",
        )

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    if quantity > product.stock:
        raise HTTPException(
            status_code=400,
            detail=f"Only {product.stock} units are available",
        )

    cart_item.quantity = quantity
    db.commit()

    return RedirectResponse("/cart", status_code=303)


@app.post("/cart/remove/{product_id}")
def remove_from_cart(
    product_id: int,
    db: Session = Depends(get_db),
):
    cart_item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == get_cart_id(),
            CartItem.product_id == product_id,
        )
        .first()
    )

    if cart_item:
        db.delete(cart_item)
        db.commit()

    return RedirectResponse("/cart", status_code=303)


@app.post("/cart/clear")
def clear_cart(db: Session = Depends(get_db)):
    (
        db.query(CartItem)
        .filter(CartItem.cart_id == get_cart_id())
        .delete(synchronize_session=False)
    )

    db.commit()

    return RedirectResponse("/cart", status_code=303)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "ShapDrop",
    }
