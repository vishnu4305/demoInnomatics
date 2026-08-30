# #Print numbers 1–10

# n=10
# for i in range(1,n+1):
#     print(i)
    
# #Print numbers 10–1.

# n = 10 
# for i in range(n,0,-1):
#     print(i)

# #Print all even numbers from 1–20.
# for i in range(1,21):
#     if i % 2 == 0:
#         print("Even ",i)
#     else:
#         print("Odd",i)


# #Ask the user for n and print numbers from 1 to n.
# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     print(i)

# # 6. Sum
# # Ask for n.
# # Calculate: 1 + 2 + 3 + ... + n

# n=int(input("Enter a number :"))
# sum=0
# for i in range(1,n+1):
#     sum += i
# print(f"{sum}")

# # 7. Multiplication Table
# # Ask for a number.
# # For example:
# # Enter number: 5
# # 5 × 1 = 5
# # 5 × 2 = 10
# # ...
# # 5 × 10 = 50

# n = int(input("Enter a number :"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")


# # Count Numbers
# # Ask for n.
# # Count how many numbers between 1 and n are divisible by 3.
# n = int(input("Enter a number :"))
# count =0
# for i in range(1,n+1):
#     if i % 3 == 0:
#         count+=1
# print(count)

# # 9. Factorial
# # Ask for a number.
# # Example:
# # 5! = 5 × 4 × 3 × 2 × 1  ==== 120

# n = int(input("Enter a number :"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(f"{n}! = {fact}")
    
# # Reverse Countdown
# # Ask for a number.

# n = int(input("Enter a number :"))
# for i in range(n,0,-1):
#     print(i)

# #Calculate the sum of all even numbers from 1 to n.
# n = int(input("Enter a number :"))
# sum =0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum += i
# print(f"Sum = {sum}")

# #Calculate the sum of all odd numbers from 1 to n.
# n = int(input("Enter a number :"))
# sum =0
# for i in range(1,n+1):
#     if i % 2 != 0:
#         sum += i
# print(f"Sum = {sum}")

# # 13. Prime Number
# # Ask for a number and determine whether it is prime.
# n = int(input("Enter a number to check prime number  or not :"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count+=1
# if count == 2:
#     print("prime")
# else:
#     print("Not a prime")

# # Give the user 3 attempts to enter the correct password.
# # Rules:
# # Correct → Login successful
# # Wrong → Try again
# # 3 wrong attempts → Account locked
# ori_password = "vishnu"
# count = 0
# for i in range(1,4):
#     count+=1
#     pa_word = input("Enter your password:")
#     if pa_word == ori_password:
#         print("Login Succesful")
#         break
#     elif count == 3:
#         print("3 wrong attempts → Account locked")
#     else:
#         print("Try again")


# # Student Marks Analyzer
# # Ask the user:
# # How many students?
# # Suppose they enter:5
# # Then repeatedly ask for marks:

# # Enter marks for student 1:
# # Enter marks for student 2:
# # Enter marks for student 3:
# # Enter marks for student 4:
# # Enter marks for student 5:

# # Calculate:

# # Total marks
# # Average marks
# # Highest marks
# # Lowest marks
# # Number of passes
# # Number of fails

# # Rules:

# # marks >= 50 → Pass
# # marks < 50  → Fail

# n = int(input("How many students?"))
# total = 0
# highest_marks = 0
# low_marks = 0
# cou_pass = 0
# cou_fail =0 
# for i in range(1,n+1):
#     student = int(input((f"Enter marks for student {i} :")))
#     total +=student
#     if student >= 50 :
#         cou_pass+=1
#         if highest_marks <=student:
#             highest_marks = student
#         if low_marks >= student:
#             low_marks = student
        
             
#     else:
#         cou_fail+=1
        
    
    
# Avg =(total)/n 
# print(f"""
#     Total marks       :{total}
#     Average marks     :{Avg}
#     Highest marks     :{highest_marks}
#     Lowest marks      :{low_marks}
#     Number of passes  :{cou_pass}
#     Number of fails   :{cou_fail}
#       """)
    
