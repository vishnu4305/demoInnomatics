# n=int(input("Enter a Number : "))
# for i in range(1,n+1):
#     print(i , end=" ")



# m=int(input("Enter a Number : "))
# n=int(input("Enter a Number : "))
# for i in range(m,n+1):
#     print(i , end=" ")



# n=int(input("Enter a Number : "))
# for i in range(n,0,-1):
#     print(i , end= " ")


# n=int(input("Enter a Number : "))
# m=int(input("Enter a Number : "))
# for i in range(n,m-1,-1):
#     print(i , end=" ")

# n = int(input("Enter a Number : "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# n = int(input("Enter a number to calculate factorial :"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

# m=int(input("Enter a Number : "))
# n=int(input("Enter a Number : "))
# sum = 1
# for i in range(m,n+1):
#     sum *= i
# print(sum)

# n=int(input("Enter a Number to print factors: "))
# count =0
# for i in range(1,n+1):
#     if n % i == 0:
#         count +=1
# print(count)
    
# n = int(input("Enter a Number to prime or not :"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")

# m =int(input("Enter a Number : "))
# n = int(input("Enter a Number : "   ))
# count_even = 0
# count_odd = 0
# for i in range(m , n+1):
#     if i % 2 ==0 :
#         count_even +=1
        
#     else:
#         count_odd +=1
# print(f"Even numbers count :{count_odd}")
# print(f"odd numbers count :{count_even}")

# s = input("Enter a string to reverse: ")
# for i in s[::-1]:
#     print(i, end=" ")
    

# s = input("enter a string")
# var = s[::-1]
# if s == var:
#     print("Palindrome")
# else:
#     print("not in Palindrome")

# n = int(input("enter a number"))
# total = 1
# while n > 0:
#     digit = n % 10
#     total *= digit
#     n //= 10
# print(total)

# n = int(input("Enter a number : "))
# original = n
# arm_num = 0
# while n>0 :
#     digit = n % 10
#     arm_num+=digit**3
#     n//=10
# if arm_num==original :
#     print("its armstrong number ")
# else:
#     print("not a armstrong number")
    
    
# n=int(input())
# orig_dig = n
# rev=0
# while n > 0:
#     digit = n % 10
#     rev=rev*10+digit
#     n//=10
# if orig_dig == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# n=(input("Enter a string:"))
# count=0
# ccount=0
# for i in n:
#     if i in "aeiou":
#         ccount+=1
#     else:
#         count+=1
# print("Vowels Count = ",ccount)
# print("Count = ",count)

# n = int(input())
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")

# n=int(input("Enter a number :"))
# sq = n*n
# sum = 0
# print(sq)
# while sq > 0:
#     digits = sq % 10
#     sum += digits
#     sq //= 10
# print(sum)
# if sum == n:
#     print("Neon Number")
# else:
#     print("Not a Neon Number")

# n = int(input("Enter a number:"))
# origi_digit = n
# total = 0
# while origi_digit > 0:
#     digit = origi_digit % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact = fact * i
#     total = total + fact
#     origi_digit = origi_digit // 10
# if total == n:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")

# n=int(input("Enter a number:"))
# origi_digit = n
# sum=0
# while n>0:
#     digit = n % 10 
#     sum += digit
#     n //= 10
# if origi_digit % sum == 0:
#     print("Harshad number")
# else:
#     print("not a harshad number")

# a =0
# b=1
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(a,end=" ")
#     c = a+b
#     a,b = b,c



    
