def login(user,passwrd):
    attempts = 0
    while attempts < 3:
        username = input("Enter your username")
        password = input("Enter your password")
        if username == user and password == passwrd:
            print("Login succesful")
            break
        else:
            attempts +=1
            print(f"Remaining attempts :{3-attempts}")
            print("Please try again")
    if attempts == 3:
        print("You have used all 3 login attempts.")
        print("Account Locked!")
    
def validation(name, email, phone, address, password):
    if name.isalpha():
        if email.islower() and email.endswith(".com") or email.endswith(".in") and email.count("@") == 1:
            if phone.isdigit() and len(phone) >=10:
                if len(password) >=8 :
                    uppercount = 0
                    lowercount = 0
                    digitcount = 0
                    specialcount =0
                    for i in password:
                        if i.isupper():
                            uppercount+=1
                        elif i.islower():
                            lowercount+=1
                        elif i.isdigit():
                            digitcount+=1
                        elif "@" in password or "#" in password or "_" in password :
                            specialcount+=1
                        
                    if uppercount >=1 and lowercount >=1 and specialcount >=1 and digitcount >=1:
                        print(f"Your username is {email.split("@")[0]}")
                        login(email.split("@")[0],password)
                    else:
                        print("Enter Alphabet ,digit and special character atleast once ")
                else:
                    print("Password should contain atleast 8 characters")
            else:
                print("Enter only digits for phone number")
        else:
            print("Enter a valid email ID")
    else:
        print("Name should have only alphabets")


def registration():
    name = input("Enter your name:")
    email = input("Enter your email:")
    ph = input("Enter your phone no:")
    address = input("Enter your address")
    password = input("Enter your password:")
    retype = input("Enter your password again:")
    if password == retype:
        validation(name,email,ph,address,password)
    else:
        print("Password not matched.")

registration()
