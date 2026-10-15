vip_list = ["Rahul", "Ananya", "Sneha", "Vikram"]
regular_list = ["Amit", "Pooja", "Rohan", "Kavya"]
user_name = input("Enter Your Name:")
user_age = int(input("Enter Your Age:"))
user_pass_type = input("Enter Your Pass Type Type (VIP or Regular):  ")

if user_pass_type == "VIP" :
    if user_name in vip_list:
        if user_age >= 18:
            print("Access Granted to VIP Zone ") 
        else:
            print("VIP Pass valid, but must be 18+ to enter!")
    else:
        print ("Fraudulent VIP Pass detected ")
    
        
    
if user_pass_type == "Regular":
    if user_name in regular_list:
        if user_age >= 18:
                    print("Access Granted to VIP Zone ") 
    else:
        print("Invalid Regular Ticket ")
        