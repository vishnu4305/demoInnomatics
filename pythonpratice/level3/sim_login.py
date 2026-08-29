user = input("Enter Your username :")
pass_w = input("Enter your password :")

correct_username = "admin"
correct_password = "python123"

if user == correct_username and pass_w == correct_password:
    print("Login Successful")
elif user == correct_username and pass_w != correct_password:
    print("Invaild password")
elif user != correct_username and pass_w == correct_password:
    print("Invaild username")
else:
    print("Invalid username and password ")