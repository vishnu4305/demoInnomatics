items =[ ]
items_price= [ ]
GST = 0
Subtotal = 0
Grand_Total = 0
print("------Innomatics Grocery Store------  ")
User_name = input("Enter Your Name : ")
print(f"{User_name} , Welcome to Innomatics Store ")
print("""
      Available items:
        1. Apple  -120
        2. Milk   -65
        3. Bread  -40
        4. Done and Exit.... 
      """)
while True:
    user_input = input("Enter item name (or 'done' to stop): ")
    
    if user_input != "done" :
      items.append(user_input)
      items_price.append(int(input("Enter item price : ")))
      print()
    else:
      break
    
for price in items_price:
  Subtotal+= price
GST =( 18/100 )*Subtotal 
Grand_Total = (GST + Subtotal)
    
print(f"{User_name}, Innomatics Store Grocery Receipt ")
print(""" 
=====================================================
                  GROCERY RECEIPT          
=====================================================

      """)

print("ITEMS PURCHASED: ",*items)
print("------------------------------------")
print("ITEM PRICES:",*items_price)
print("------------------------------------")
print(f"SubTotal : {Subtotal}")
print(f"Gst (18%) : {GST}")
print("------------------------------------")
print(f"Grand Total : {Grand_Total}")
print("====================================")
print(f"{User_name},**Thank you for your purchase! Your support means a lot to us. We look forward to welcoming you back for your next shopping trip.**")
