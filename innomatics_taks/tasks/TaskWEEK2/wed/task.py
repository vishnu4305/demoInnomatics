print("-----------------------------")
print("-----------------------------")
for i in range(1,11):
    print(f"{i} :Python")
print("")



print("-----------------------------")
print("-----------------------------")

print("Countdown:")
for i in range(10,0,-1):
    print(f"{i}")


print("-----------------------------")
print("-----------------------------")
for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i)
   
print("-----------------------------")
print("-----------------------------") 
user_name = "admin"
user_password = "Python123"
while True:
    user_input = input("Enter password: ")
    if user_input == user_password:
        print("Welcome to python classs")
        break

print("-----------------------------")
print("-----------------------------")
print("Menu:")
print("""   1. Play
            2. Settings
            3. Exit""")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        continue
    elif choice == 2:
        continue
    elif choice == 3:
        print("Welcome again! Have a nice day.")
        break
    else:
        print("Invalid choice")