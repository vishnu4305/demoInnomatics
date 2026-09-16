registered_students = set()
while True:
    user_name = input("Enter Your Name (Or done to Exit):")
    if user_name == "done":
        break
    else:
        registered_students.add(user_name)
    print("Currect list:",registered_students)
print("===Final REgistration List===")
print("Currect List :")
for i , Value in enumerate(registered_students):
        print(f"  {i+1} . {Value} ")
print(f"Total unique students registered :{len(registered_students)}")
user_check = input("Enter a name to check : ")
if user_check in registered_students:
    print("Already registered.")
else:
    print("Not registered.")