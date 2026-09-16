import mysql_data
from users import user
from rest import restaurant_bill

# Connect to MySQL
connection = mysql_data.mysqlabc()
pen = connection.cursor()
user_name = user()
print(f"\nWelcome, {user_name}!")
user_query = """
INSERT INTO users (user_name)
VALUES (%s)
"""
pen.execute(user_query, (user_name,))
connection.commit()

user_coupon, subtotal, subcoupon, gst, grand_total = restaurant_bill()

order_query = """
INSERT INTO orders
( coupon, subtotal, discount, gst, grand_total)
VALUES ( %s, %s, %s, %s, %s)
"""

order_values = (
    user_coupon,
    subtotal,
    subcoupon,
    gst,
    grand_total
)
pen.execute(order_query, order_values)
connection.commit()

print("\n Order saved successfully in MySQL!")
connection.close()