
from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from database import Base


# Product Model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(50))
    stock = Column(Integer, default=0)
    image_url = Column(String(255))

    # Relationship with cart items
    cart_items = relationship(
        "CartItem",
        back_populates="product",
        cascade="all, delete-orphan",
    )


# Shopping Cart Item Model
class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cart_id = Column(String(64), nullable=False, index=True)
    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
    )
    quantity = Column(Integer, default=1, nullable=False)

    # Relationship with Product
    product = relationship(
        "Product",
        back_populates="cart_items",
    )
