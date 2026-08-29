pro = input("Enter Your Product name :")
pro_w = int(input("Enter your product price :"))
quan = int(input("Enter quantity :"))

subtotal = pro_w * quan
discount = 0
if subtotal >= 5000:
    discount = subtotal * (20/100)
    print("20% discounr applied")
elif subtotal >= 2000:
    discount = subtotal * (10/100)
    print("10% discounr applied")
else:
    print("No discount")
    
Fina_am = subtotal - discount 
    
print(f"""
Product      : {pro}
Quantity     : {quan}
Subtotal     : {subtotal}
Discount     :{discount}
Final Amount :{Fina_am}
""")