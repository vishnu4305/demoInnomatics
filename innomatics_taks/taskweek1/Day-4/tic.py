Member = input("Is your birthday Today?: ")
if Member == "yes":
    print("Happy Birthday! You are eligible for a free ticket.")
else:
    print("You are not eligible for a free ticket.")    
    age = int(input("Enter your age: "))
    price = 0
    if age <= 3:
        print("You are eligible for a free ticket.")
    elif age >= 4 and age <= 12:
        price = 150
        print(f"The ticket price is ${price}.")
    elif age >= 13 and age <= 64:
        price = 250
        print(f"The ticket price is ${price}.")
    else:
        price = 300
        print(f"The ticket price is ${price}.")



