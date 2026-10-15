user_name = input("Enter your full name :")
user_gmail =input("Enter your email :")
user_phone = input("Enter your Ph No :")
user_city =input("Enter your city :")
user_fav = input("Enter your favourite technology :")
user_skill =input("Enter your skills separated by comma :")

print(user_name.title())
print(user_city.title())
print(user_gmail.lower())

# part-2

user_r=user_gmail.find("@")
user_g =user_gmail[0:user_r].lower()
print("Generated Username :",user_g)
# part-3

print("---------- EMAIL ANALYSIS ----------")
print("Email:",user_gmail)
print("Starts with user :",user_gmail.startswith(user_name))
print("Ends with .com : ",user_gmail.endswith("@gmail.com"))
print("@ position : ",user_r)
print("Last . position : ",user_gmail.rfind("."))
print("Number of dots : ",user_gmail.count("."))

# part-4

skill_p = user_skill.split(",")
skill_j = "|".join(skill_p)
skill_title= skill_j.title()
print(skill_title)


# part-5
print("""
================================
    CODEHUB PROFILE
================================
      """)
print("Name :",user_name )
print("Username : ",user_g)
print("Email : ",user_gmail)
print("Phone : ",user_phone)
print("City :",user_city)
print("Technology :",user_fav )
print("Skills : ",skill_title)
print("""
================================
PROFILE CREATED!
================================
""")

# part-6
dev_ida ="".join(user_name[0:4])
dev_idb="".join(user_city[0:4])
dev_idc="".join(user_fav[0:3])
dev_id = (dev_ida+dev_idb+dev_idc).upper()
print("Developer Id :",dev_id)


# part-7
sec_c = input("Enter Role :")
print("Security Check :",sec_c.swapcase())

# part-8

print("CAse-Insensitive check :",user_fav.casefold())


# Part-9

user_fin = input("Enter a piece of text from the user's name : ")

print(user_name.find(user_fin))
print(user_name.rfind(user_fin))
print(user_name.count(user_fin))

# part-10
print("""
================================
        WELCOME TO CODEHUB
================================
Learn Python.
Build APIs.
Create React applications.
Become a Full Stack Developer.

      """)

#Mini Project 
print("""
========================================
            CODEHUB USER REGISTRATION
========================================
      """)
print("Enter your full name:",user_name)
print("Enter your email:",user_gmail)
print("Enter your phone number:",user_phone)
print("Enter your city:",user_city)
print("Enter your favourite technology:",user_fav)
print("Enter your skills:",user_skill)
print("""
      Processing profile...
========================================
            PROFILE
========================================
      """)
print("Name :",user_name)
print("Username :",user_g)
print("Email :",user_gmail)
print("Phone :",user_phone)
print("City :",user_city)
print("Technology :",user_fav)
print("Skills :",user_skill)
print("""
========================================
            EMAIL ANALYSIS
========================================
      """)
print("Starts with username :",user_gmail.startswith(user_name))
print("Ends with .com : ",user_gmail.endswith(".com"))
print("@ position : ",user_r)
print("Last . position : ",user_gmail.rfind("."))
print("Number of dots : ",user_gmail.count("."))


print("""
===============================================
            DEVELOPER INFORMATION
===============================================
      """)

print("Developer Id :",dev_id)

print("Security Check :",sec_c.swapcase())
