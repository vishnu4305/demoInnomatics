menu_items = ["Burger", "Pizza", "Pasta", "Fries", "Coke"]
menu_prices = [100, 250, 180, 90, 50]
ordered_items = []
ordered_prices = []
Coupons = ["SAVE10", "WELCOME50"]
Subtotal = 0
Subcoupon = 0
print("Available Items")
for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")
while True:
    user_input = input("Enter items one by one: ")
    if user_input == "done":
        break
    if user_input in menu_items:
        item_index = menu_items.index(user_input)
        ordered_items.append(menu_items[item_index])
        ordered_prices.append(menu_prices[item_index])
    else:
        print("Invalid Item Name")

for i in ordered_prices:
    Subtotal += i
print("\nAvailable Coupons")
for i in range(len(Coupons)):
    print(f"{i+1}. {Coupons[i]}")
user_coupon = input("Choose Coupon: ")
if user_coupon == "SAVE10":
    print("Applied 10% discount")
    Subcoupon = Subtotal / 10
elif user_coupon == "WELCOME50":
    print("Flat ₹50 discount")
    Subcoupon = 50
else:
    print("No coupon available")
Discounted_Total = Subtotal - Subcoupon
GST = Discounted_Total * 18 / 100
GrandTotal = Discounted_Total + GST
print("""
========================================
      RESTAURANT BILLING System
========================================""")
for i in range(len(ordered_items)):
    print(f"{i+1}. {ordered_items[i]} : ₹{ordered_prices[i]}")
print("----------------------------------------")

print(f"Subtotal       : ₹{Subtotal}")
print(f"Discount       : -₹{Subcoupon}")
print(f"Amount         : ₹{Discounted_Total}")
print(f"GST (18%)      : +₹{GST}")
print(f"Grand Total    : ₹{GrandTotal}")
print("""
========================================
      Thank You! Visit Again"
========================================""")