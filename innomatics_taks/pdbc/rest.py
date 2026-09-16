def restaurant_bill():
    menu_items = ["Burger", "Pizza", "Pasta", "Fries", "Coke"]
    menu_prices = [100, 250, 180, 90, 50]
    ordered_items = []
    ordered_prices = []

    coupons = ["SAVE10", "WELCOME50"]

    subtotal = 0
    subcoupon = 0

    print("\n========== AVAILABLE ITEMS ==========")

    for i in range(len(menu_items)):
        print(f"{i + 1}. {menu_items[i]} - ₹{menu_prices[i]}")

    while True:
        user_input = input("\nEnter item name one by one (or 'done'): ")

        if user_input.lower() == "done":
            break

        if user_input in menu_items:

            item_index = menu_items.index(user_input)

            ordered_items.append(menu_items[item_index])
            ordered_prices.append(menu_prices[item_index])

            print(f"{user_input} added to order.")

        else:
            print("Invalid item name!")

    # Calculate subtotal
    for price in ordered_prices:
        subtotal += price

    # Coupons
    print("\n========== AVAILABLE COUPONS ==========")

    for i in range(len(coupons)):
        print(f"{i + 1}. {coupons[i]}")

    user_coupon = input("\nChoose coupon (or enter NONE): ").upper()

    if user_coupon == "SAVE10":

        print("Applied 10% discount.")
        subcoupon = subtotal * 10 / 100

    elif user_coupon == "WELCOME50":

        print("Applied flat ₹50 discount.")
        subcoupon = min(50, subtotal)

    else:

        print("No coupon applied.")
        user_coupon = None
        subcoupon = 0
    discounted_total = subtotal - subcoupon
    gst = discounted_total * 18 / 100

    grand_total = discounted_total + gst

    # Bill
    print("""
========================================
       RESTAURANT BILLING SYSTEM
========================================
""")

    for i in range(len(ordered_items)):
        print(f"{i + 1}. {ordered_items[i]} : ₹{ordered_prices[i]}")

    print("----------------------------------------")

    print(f"Subtotal       : ₹{subtotal:.2f}")
    print(f"Discount       : -₹{subcoupon:.2f}")
    print(f"Amount         : ₹{discounted_total:.2f}")
    print(f"GST (18%)      : +₹{gst:.2f}")
    print(f"Grand Total    : ₹{grand_total:.2f}")

    print("""
========================================
          Thank You! Visit Again
========================================
""")

    # Return values to main.py
    return user_coupon, subtotal, subcoupon, gst, grand_total