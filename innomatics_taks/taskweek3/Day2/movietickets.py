booking = []
Movie_names = ["DC ", "spider-man", "Tosic" ,"channai-Lovestory" ]
user_name = input("Enter Your Name :")
total = 0
while True:
    print(f"{user_name} , Welcome to the innomatics movies ...")
    print("Available Movies")
    for i , Values in enumerate(Movie_names):
            print(f"{i+1} . {Values}")
    Movie_name = input("Enter Movie Name: ")
    seat_number = input("Enter Prefer Seat :")
    price = int(input("Enter Price of the Movie :"))
    
    total += price    
    Ticket = (Movie_name , seat_number , price)
    
     
    user_more_ticket = input("Do You to Book ONe more Ticket (Yes/No):")
    booking.append(Ticket)
    
    if user_more_ticket == "Yes":
        print("yes")
    else:
        break

print("  ======= All Booking =======")
for ticket in booking:
    name,seat,price = ticket
    print(f"   {name} | {seat} | Rs . {price}")
print(f"Total tickets Booked : {len(booking)}" )
print(f"Total amount collected : Rs . {total}")

        

    

    
    
            
    
    