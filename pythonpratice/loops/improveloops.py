# # Number Sequence 1-50
# for i in range(1,51):
#     print(i)
    
# # reverse 50 -1
# for i in range(50,0,-1):
#     print(i)

# #even numbers 
# for i in range(2,51,2):
#     print(i)

# #Odd Numbers 
# for i in range(1,50,2):
#     print(i)

# #multi 5 numbers 
# for i in range(5,101,5):
#     print(i)

# #Task 6 — Sum
# n = int(input("Enter n :"))
# sum_n = 0
# for i in range(0,n+1):
#     sum_n+=i
# print(sum_n)

# #Task 7 — Even Sum  Ask for n.

# n = int(input("Enter numer :"))
# sum_n = 0 
# for i in range(2,n+1,2):
#     sum_n+=i
# print(sum_n)

# # Task 8 — Odd Sum
# # Same thing, but odd numbers.
# n = int(input("Enter numer :"))
# sum_n = 0 
# for i in range(1,n+1,2):
#     sum_n+=i
# print(sum_n)

# #Task 9 — Square Sum
# n = int(input("enter a number :"))
# sum_sq = 0
# for i in range(n+1):
#     sum_sq += i*i
# print(sum_sq)

# #Task 10 — Count Divisibility
# n = int(input("Enter a number :"))
# count_3 = 0
# count_5 = 0
# for i in range(1,n+1):
#     if i % 3 == 0:
#         count_3+=1
#     if i % 5 == 0:
#         count_5 +=1
# print(f"Divisible by 3 = {count_3}")
# print(f"Divisible by 5 = {count_5}")

# #Task 11 — Countdown
# n = int(input("Enter starting number :"))
# while n>=1:
#     print(n)
#     n -= 1

# # task 12 — Countdown
# n = int(input("Enter starting number :"))
# i =1
# while i <= n:
#     print(i)
#     i += 1
    
    
# #Task 13 — Password Loop
# cor_pass = "vishnu"

# while True:
#     user_pass = input("Enter your password :")
#     if user_pass == cor_pass:
#         print("login Successful")
#         brack

# #Task 14 — Number Guessing
# secret_num = 7
# while True:
#     n = int(input("Guess the number :"))
#     if n != secret_num:
#         print("Wrong! Try again.")
#     else:
#         print("Correct ! You guessed it.")
#         break

# # Task 15 — Stop at 7 Print numbers 1-10
# i = 1
# n = int(input("Enter a number to stop :"))
# while True:
#     if i == n:
#         break
#     print(i)
#     i+=1

# # Task 16 — Skip 5
# i=1
# n = int(input("enter a number to skip :"))
# while i<=10:
#     if i == n:
#         i+=1
#         continue
#     print(i)
#     i+=1
# #multiple of n is skiped
# n= int(input("enter a number :"))
# for i in range (1,31):
#     if i % n == 0:
#         continue
#     print(i)

# # Task 18 — Stop at Negative
# while True:
#     n = int(input("Enter a number :"))
#     if n<=0:
#         print("Negative number Detected")
#         print("Program stopped")
#         break


# #Task 19 — Positive Number Sum
# sum_n = 0
# while True:
#     n=int (input("enter a number to add or -1 for stop:"))
#     if n >=0:
#         sum_n += n
#     else:
#         break
# print(sum_n)

# #Task 20 — Find Highest
# high_num = 0
# m=int(input("How many numebrs? :"))
# for i in range(m):
#     n = int(input("Enter "))
#     if high_num < n:
#         high_num = n
# print(high_num)
    

# #Task 21 — Find Lowest

# m=int(input("How many numebrs? :"))
# low_num = int(input("Enter "))
# for i in range(1,m):
#     n = int(input("Enter "))
#     if int(low_num) > n:
#         low_num = n
# print(low_num)


# # Task 22 — Highest + Lowest
# count = int(input("enter a number :"))
# n = int(input("Enter :"))
# total = n
# high_num = n
# low_num = n
# for i in range(1,count):
#     m = int(input("Enter :"))
#     low_num = m
#     if high_num < m:
#         high_num = m
#     if low_num > m:
#         low_num = m
#     total+=m
# avg = total/count
# print(f"""
# Total : {total}
# Average :{avg}
# highest : {high_num}
# lowest : {low_num}
# """)

# # ==================================================================
# #Task 23 — Pass/Fail Analyzer

# n = int(input("how many students:"))

# total = 0
# high_mark = None
# low_marks = None
# pass_count = 0
# fail_count = 0

# if n <= 0:
#     print("Invaild input")
# else:
#     for i in range(n):
#         while True:
#             st = int(input(f"Enter {i+1} student marks :"))
#             if st >100 or st <0:
#                 print("Invaild input for marks")
#                 continue
#             else:
#                 break
#         total += st
#         if high_mark is None or st > high_mark:
#             high_mark = st
#         if low_marks is None or st < low_marks:
#             low_marks = st
#         if st >= 50 :
#             pass_count += 1
#         else:
#             fail_count += 1

# if n > 0:
#     avg = total / n
#     print(f"""

#     Total    :{total}
#     Average  : {avg}
#     Highest  :{high_mark}
#     Lowest   :{low_marks}
#     Pass count:{pass_count}
#     Fail count:{fail_count}

#         """)

# #Challenge a - count digits
# n = int(input("Enter a number :"))
# count = 0
# while n > 0:
#     diff = n % 10 
#     count += 1
#     n = n // 10
# print(count) 

# # Challenge B — Reverse a Number
# n = int(input("Enter a number :"))
# reverse = 0

# while n > 0:
#     diff = n % 10 
#     reverse = reverse * 10 + diff
#     n = n // 10
# print(reverse)

# #Challenge C — Sum of Digits
# n = int(input("Enter  a  number :"))
# sum_n = 0
# while n > 0:
#     diff = n % 10
#     sum_n += diff
#     n = n // 10
# print(sum_n)

# #Challenge D — Count Even/Odd Digits

# n = int(input("Enter  a  number :"))
# even_n = 0
# odd_n = 0
# while n > 0:
#     diff = n % 10
#     if diff % 2 == 0:
#         even_n+=1
#     else:
#         odd_n+=1
#     n = n // 10
# print(f"Even Digits = {even_n}")
# print(f"Odd Digits = {odd_n}")





# #=========================================================
# #=========================================================


# # Task 1 
# n = int(input("enter a number :"))

# count_n= 0
# if n == 0:
#     count_n = 1

# while n > 0:
#     diff = n % 10 
#     count_n += 1
#     n = n // 10
# print(count_n)

# #reverse a number 
# n = int(input("enter a number :"))
# rev = 0
# while n > 0:
#     diff = n % 10
#     rev = rev * 10 + diff  
#     n = n // 10
# print(rev)



# #sum until zero
# sum_n = 0
# while True :
#     n = int(input("Enter a number :"))
#     if n != 0:
#         sum_n += n
#     else:
#         break
# print(sum_n)

# #Skip Negative Numbers


# sum_n = 0
# while True:
#     n = int(input("Enter a number :"))
#     if n > 0:
#         sum_n += n
#     elif n == 0:
#         break
#     else:
#         continue
# print(sum_n)

# #Password + 3 Attempts
# ori_pass = "vishnu"
# count_p = 0
# while True:
#     count_p += 1
    
#     if count_p <= 3 :
#         n = input("enter your password :")
#         if n == ori_pass:
#             print("Login Sussceful")
#             break
#         else:
#             continue
#     else:
#         print("Account Blocked")
#         break
    
# #Task 6 — Find Highest Until -1

# while True:
#     n = int(input("Enter a number :"))
#     high_num = n
#     if n == -1:
#         print("Stopped . And Highest number =",high_num)
#         break
    
#     if high_num <= n:
#         high_num = n

# # ☠️ Task 8 — Ultimate Loop Challenge

sum_n = 0
high_n = None
low_n = None
count_even = 0
count_odd = 0
while True:
    print(f"""
=========================
      NUMBER ANALYZER
=========================

1. Enter Number 
2. Show Sum
3. Show Highest
4. Show Lowest
5. Show Even Count
6. Show Odd Count
7. Exit
      """)
    m = int(input("Enter number:"))
    if m == 1:
        n = int(input("Enter a number :"))
        if n > 0:
            sum_n += n
            
            if high_n is None :
                print("Number is not enterd. ")
            else:
                high_n = n
            if low_n is None :
                print("Number is not enterd. ")
                
            else:
                low_n = n
            if n % 2 == 0:
                count_even += 1
            elif n % 2 != 0:
                count_odd += 1
            else:
                print("Invaild number . Try again")
        else:
            print("Enter Positive numbers Only ")
    elif m == 2:
        print(sum_n)
    elif m == 3:
        print(high_n)
    elif m == 4:
        print(low_n)
    elif m == 5:
        print(count_even)
    elif m == 6:
        print(count_odd)
    elif m==7:
        print("Exit")
        break
    else:
        print("Enter a vaild number.")
    
        

    
