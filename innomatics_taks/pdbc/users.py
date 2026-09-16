def user():
    user_name = input("Enter Your name ")
    return user_name
# import datetime

# class BikeShop:
#     def __init__(self, stock=0):
#         """Initializes the bike shop with a given stock of bikes."""
#         self.stock = stock

#     def display_stock(self):
#         """Displays the total number of bikes available for rent."""
#         print(f"We currently have {self.stock} bikes available for rent.")
#         return self.stock

#     def rent_bikes(self, count):
#         """Rents out a specified number of bikes and notes the timestamp."""
#         if count <= 0:
#             print("Number of bikes should be greater than zero.")
#             return None
#         elif count > self.stock:
#             print(f"Sorry! We only have {self.stock} bikes available to rent.")
#             return None
#         else:
#             now = datetime.datetime.now()
#             print(f"You have rented {count} bike(s) today at {now.strftime('%H:%M:%S')}.")
#             print("You will be charged $5 per hour per bike.")
#             self.stock -= count
#             return now

#     def return_bikes(self, rental_time, count):
#         """Accepts returned bikes, updates stock, and calculates the bill."""
#         if rental_time and count:
#             self.stock += count
#             now = datetime.datetime.now()
#             rental_period = now - rental_time
            
#             # For demonstration purposes, we assume 1 hour has passed if the time is very short
#             hours = max(1, round(rental_period.total_seconds() / 3600))
#             bill = hours * 5 * count
            
#             print(f"Thanks for returning your bike(s).")
#             print(f"Total rental duration: {hours} hour(s).")
#             print(f"Your total bill is: ${bill}")
#             return bill
#         else:
#             print("Are you sure you rented bikes from us?")
#             return None

# class Customer:
#     def __init__(self):
#         self.bikes = 0
#         self.rental_time = None

#     def request_bikes(self, count):
#         """Customer requests a specific number of bikes."""
#         self.bikes = count
#         return self.bikes

#     def return_bikes(self):
#         """Customer returns the rented bikes."""
#         if self.bikes and self.rental_time:
#             return self.rental_time, self.bikes
#         else:
#             return 0, 0

# # --- Demonstration of the Code ---
# if __name__ == "__main__":
#     # Initialize shop with 10 bikes and a customer
#     shop = BikeShop(stock=10)
#     customer = Customer()

#     # 1. Check shop inventory
#     shop.display_stock()
#     print("-" * 40)

#     # 2. Customer requests and rents 2 bikes
#     requested_count = customer.request_bikes(2)
#     customer.rental_time = shop.rent_bikes(requested_count)
#     print("-" * 40)

#     # 3. Check inventory again to verify reduction
#     shop.display_stock()
#     print("-" * 40)

#     # 4. Customer returns the bikes
#     rental_time, count = customer.return_bikes()
#     shop.return_bikes(rental_time, count)