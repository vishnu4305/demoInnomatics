addhar = {}
name = input("Enter your name: ")
addhar['name'] = name

addhar_no = int(input("Enter your addhar number: "))
addhar['addhar_no'] = addhar_no

addhar_dob =input("Enter your addhar dob :")
addhar['addhar_dob'] = addhar_dob


#Nested Dist
addhar_details ={ }

addhar_add = input("Enter your address : ")
addhar_details['addhar_add'] = addhar_add

addhar_pincode = int(input("Entere your pincode :"))
addhar_details['addhar_pincode'] = addhar_pincode


gender =input("Enter your gender  (Male /Female):")
addhar["gender"] = gender

addhar['addhar_detail '] = addhar_details
print(addhar)