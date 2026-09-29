

# num = [10,20,35,40]
# print(num[::-1])
# #[40, 35, 20, 10]


# for i in range(len(num)):
#     print(i+1 ,num[i])
# # 1 10
# # 2 20
# # 3 35
# # 4 40

# # List + Condition
# for i in num:
#     if i % 2 == 0:
#         print(i)
# # 10
# # 20
# # 40
# # Even Numbers and odd
# numbers = [10, 15, 22, 31, 40, 55, 60]
# for i in numbers:
#     if i % 2 != 0:
#         print(i)

# # Create an Even Numbers List
# numbers = [10, 15, 22, 31, 40, 55, 60]
# even = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# # Task 6 — Positive and Negative Lists
# numbers = [10, -5, 20, -8, 0, 15, -3, 7]
# positive =[]
# negative =[]
# for i in numbers:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
# print(f"""
#     Positive :{positive}
#     Negative :{negative}
# """)

# # Task 7 — Sum of Positive Numbers
# numbers = [10, -5, 20, -8, 0, 15, -3, 7] 
# sum_n = 0
# for i in numbers:
#     if i > 0:
#         sum_n += i 
# print(f"Positive Sum :{sum_n}")

# #Task 8 — Count Multiples -Count how many numbers are divisible by 5.
# numbers = [10, 15, 22, 30, 40, 55, 60, 71]
# count = 0
# for i in numbers:
#     if i % 5 == 0:
#         count += 1
# print(f"Count : {count}")

# # Task 9 — Search an Element
# numbers = [10, 25, 30, 45, 50, 65]
# target = 45 
# found = False
# for i in numbers:
#     if target == i :
#         found = True        
#         break
# if found:
#     print("Found")
# else:
#     print("Not found")

# # Task 10 — First Even Number
# numbers = [11, 13, 17, 21, 24, 30, 40]
# for i in numbers:
#     if i % 2 == 0:
#         print(f"First Even :{i}")
#         break


# # Task 11 — Skip Negative Numbers
# numbers = [10, -5, 20, -8, 30, -2, 40]
# for i in numbers:
#     if i < 0:
#         continue
#     print(i)


# # Task 12 — Student Analyzer

# marks = [85, 42, 67, 91, 35, 76, 50]
# Total_Marks = 0
# Count_Passed = 0
# Count_Failed = 0
# if len(marks) == 0:
#     print("List is emety")
# else:
#     Highest_Marks = marks[0]
#     Lowest_Marks = marks[0]
#     for i in marks:
#         Total_Marks += i
#         if Highest_Marks < i:
#             Highest_Marks = i
#         if Lowest_Marks > i :
#             Lowest_Marks = i
#         if i >= 50 :
#             Count_Passed +=1
#         else:
#             Count_Failed += 1
#     print(f""" 
#     Total: {Total_Marks}
#     Highest: {Highest_Marks}
#     Lowest:{Lowest_Marks}
#     Passed: {Count_Passed}
#     Failed: {Count_Failed}
#         """)



# # Task 13 — Modify List by Index
# numbers = [10, 20, 30, 40, 50]
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         numbers[i] *= 2
# print(numbers)

# # Task 14 — Remove Invalid Marks and Valid marks are 0 to 100.
# marks = [85, 120, 45, -10, 76, 101, 50]
# new_marks = []
# for i in marks:
#     if i <= 100  and i >= 0:
#         new_marks.append(i)
#         continue
#     else:
#         continue
# print(new_marks)

# Task 15 — Transaction Analyzer            
transactions = [500, -200, 1000, -300, -150, 700, -100]
count_rev = 0
Total_rev = 0
total_net = 0
Total_spe = 0
if len(transactions) == 0:
    print("List is emety")
else:
    highest_amount = transactions[0]
    for i in transactions:
        if i > 0:
            Total_rev += i 
            count_rev += 1
            if highest_amount < i:
                highest_amount = i
        if i < 0:
            Total_spe -= i 
        total_net += i 
        
    print(f""" 
Received: {Total_rev}
Spent: {Total_spe}
Net Balance: {total_net}
Received Transactions: {count_rev}
Highest Received: {highest_amount}
            """)

    


