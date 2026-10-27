# Q1. Division Calculator
# def divide(a, b):
#     if b == 0:
#         print("Cannot divide by zero.")
#         return

#     print(f"Result: {a / b}")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# divide(a, b)


# Q2. Login System
# def login(username, password):
#     if username != "admin" or password != "python123":
#         print("Invalid username or password")
#         return
#     print("Login Successful")
# username = input("Enter username: ")
# password = input("Enter password: ")

# login(username, password)

# # Q3. Age Validation
# def register(age):
#     if age < 18:
#         print("You must be at least 18 years old to register.")
#         return
#     print("Registration Successful")
# age = int(input("Enter your age: "))
# register(age)

# # Q4. Square Number
# square = lambda n: n ** 2
# n = int(input("Enter number: "))
# print(square(n))

# # Q5. Largest Number
# largest = lambda a, b: a if a > b else b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(largest(a, b))

# # Q6. Even or Odd
# check = lambda n: "Even" if n % 2 == 0 else "Odd"
# n = int(input("Enter number: "))
# print(check(n))

# # Q7. Grade Calculator
# grade = lambda marks: "Pass" if marks >= 35 else "Fail"

# marks = int(input("Enter marks: "))
# print(grade(marks))

# # Q8. Greeting Function
# def greetings(name):
#     print(f"Hello {name}")

# def execute(function, name):
#     function(name)

# name = input("Enter name: ")
# execute(greetings, name)

# # Q9. Calculator using Higher Order Function
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def calculate(operation, a, b):
#     return operation(a, b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# choice = input("Enter operation (+, -, *): ")
# if choice == "+":
#     result = calculate(add, a, b)
# elif choice == "-":
#     result = calculate(subtract, a, b)
# elif choice == "*":
#     result = calculate(multiply, a, b)
# else:
#     result = "Invalid operation"
# print(result)


# # Q10. Welcome Message
# def welcome(name):
#     print(f"Welcome {name}")
# def display(function, student_name):
#     function(student_name)

# name = input("Enter student name: ")
# display(welcome, name)

# # Q11. Square Every Number
# numbers = [4, 16, 36, 64, 100]
# result = list(map(lambda n: n ** 2, numbers))

# print(result)


# # Q12. Convert to Uppercase
# names = ["rahul", "anita", "john", "kiran"]
# result = list(map(lambda name: name.upper(), names))

# print(result)


# # Q13. Add 5 to Every Number
# marks = [60, 72, 81, 45, 90]
# result = list(map(lambda n: n + 5, marks))

# print(result)


# # Q14. Find String Length
# cities = ["Delhi", "Mumbai", "Chennai", "Hyderabad"]
# result = list(map(len, cities))

# print(result)

# Q15. Celsius to Fahrenheit
temperatures = [0, 10, 20, 30, 40]
result = list(map(lambda c: (c * 9 / 5) + 32, temperatures))

print(result)