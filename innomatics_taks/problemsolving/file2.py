# #3. Biggest Among Two Numbers
# #Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7
# A = int(input("Enter A :"))
# B = int(input("Enter B :"))
# C = int(input("Enter C :"))
# if A >= B and A >= C:
#     print(A)
# elif B >= A and B >= C :
#     print(B)
# else:
#     print(C)
    
# #. Perfect Square or Not 

# n = int(input("Enter a number :"))
# root = int(n ** 0.5)
# squ = root * root
# if squ == n:
#     print("Perfect root")
# else:
#     print("Not perfect root")


# #3. Cars Required for Members (Max 5 per car)
# n= int(input("Enter a Number :"))
# mem_5 = n // 5
# remaining = n-(mem_5*5)
# if remaining > 0:
#     mem_5 += 1
# print(f"Cars requide :{mem_5} ")

# # Leap Year or Not
n = int(input("Enter a number :"))

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Leap Year")
else:
    print("Not leap year ")