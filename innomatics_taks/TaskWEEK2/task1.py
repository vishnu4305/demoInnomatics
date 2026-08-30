# Smart Restaurant Billing System
print("Details of customer in the Restaurant System")
Name = input("Enter your name: ")
print(f"Hello {Name}, Welcome to our Restaurant.")
print("""Lets show the Menu of our Restaurant:
      1. Veg Biryani    - 250
      2.Chicken Biryani - 320
      3. Soft Drink     - 60
      4. Ice Cream      - 90
      5. Exit
      """)
ordercount = 0
TotalPrice = 0

Order = input("Enter your order from the menu: ")
if Order == "Veg Biryani":
    ordercount += 1
    TotalPrice += 250
    print("You have ordered Veg Biryani. The price is 250.")
elif Order == "Chicken Biryani":
    ordercount += 1
    TotalPrice += 320
    print("You have ordered Chicken Biryani. The price is 320.")
elif Order == "Soft Drink":
    ordercount += 1
    TotalPrice += 60
    print("You have ordered Soft Drink. The price is 60.")
elif Order == "Ice Cream":
    ordercount += 1
    TotalPrice += 90
    print("You have ordered Ice Cream. The price is 90.")
else:
    print("Sorry, we don't have that item on the menu.")
Packaging = input(f"Hello {Name}, do you want to order anything else sir ? (yes/no): ")
GST = 0.05 * TotalPrice
Discount = 0.1 * TotalPrice
PackagingCharge =15 * ordercount
DeliveryCharge = 20 * ordercount

if Packaging == "yes":
    print("Please place your order again.")
    Order = input("Enter your order from the menu: ")
    
if Packaging == "no":
    print("Thank you for your order. Your food will be served soon.")
    print(f"{Name},Here is your bill:")
    print(f"item-wise details of your order: {Order}")
    print(f"Total items ordered: {ordercount}")
    print(f"Total Price: {TotalPrice}")
    print(f"Packaging Charge: {PackagingCharge}")
    print(f"Delivery Charge: {DeliveryCharge}")
    print(f"GST: {GST}")
    print(f"Discount: {Discount}")
    print(f"Final Bill: {TotalPrice + PackagingCharge + DeliveryCharge + GST - Discount}")
