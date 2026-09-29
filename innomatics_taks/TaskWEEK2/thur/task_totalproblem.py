# Smart Class Analytics System

student_names = ["vishnu", "ram", "Cheran", "surya", "mani"]
student_marks = [45, 88, 92, 35, 75]
total_students = len(student_names)
print("Total Students:", total_students)
print("\nTop Student Details")
print("Name:", student_names[2])
print("Marks:", student_marks[2])
print("\nStudent Grades")
for i in range(len(student_names)):
    name = student_names[i]
    marks = student_marks[i]
    if marks >= 80:
        grade = "A (Pass)"
    elif marks >= 50:
        grade = "B (Pass)"
    else:
        grade = "F (Fail)"
    print(name, "-", marks, "-", grade)
total_marks = 0
for marks in student_marks:
    total_marks += marks
average = total_marks / len(student_marks)
print("\nClass Average:", average)
passed = 0
failed = 0
for marks in student_marks:
    if marks >= 50:
        passed += 1
    else:
        failed += 1
print("Passed Students:", passed)
print("Failed Students:", failed)


# VIP Event Access Portal
vip_list = ["vishnu", "ram", "Cheran", "surya"]
regular_list = ["sir", "hari", "Rohan", "mani"]
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
pass_type = input("Enter Pass Type (VIP/Regular): ")
if pass_type == "VIP":
    if name in vip_list:
        if age >= 18:
            print("Access Granted to VIP Zone")
        else:
            print("VIP Pass valid, but must be 18+ to enter!")
    else:
        print("Fraudulent VIP Pass detected")
elif pass_type == "Regular":
    if name in regular_list:
        if age >= 18:
            print("Access Granted to General Zone")
        else:
            print("Regular Pass valid, but must be 18+ to enter!")
    else:
        print("Invalid Regular Ticket")
else:
    print("Unknown Pass Category")

# Nested Loop Patterns
size = int(input("Enter size: "))

for row in range(size):
    for col in range(size):
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 2 — Number Staircase
height = int(input("Enter height: "))
num = 1
for row in range(1, height + 1):
    for col in range(row):
        print(num, end=" ")
        num += 1
    print()


# Pattern 3 — Hourglass
height = int(input("Enter odd height: "))

for row in range(height, 0, -2):
    spaces = (height - row) // 2
    for i in range(spaces):
        print(" ", end=" ")
    for i in range(row):
        print("*", end=" ")
    print()

for row in range(3, height + 1, 2):
    spaces = (height - row) // 2
    for i in range(spaces):
        print(" ", end=" ")
    for i in range(row):
        print("*", end=" ")
    print()

# Pattern 4 — Checkerboard
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for row in range(rows):
    for col in range(columns):
        if (row + col) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

