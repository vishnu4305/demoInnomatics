# # SECTION 1 — PYTHON / JAVA PROGRAMMING
# # 1. Reverse a String

# a = input("Enter a string :")
# rev = a[::-1]
# print(rev)


# rev1 = ""
# for i in a:
#     rev1 = i +rev1
# print(rev1)
# # Enter a string :hello
# # olleh

# # 2. Check Palindrome  [Easy]
# a = input("Enter a string :")
# # approch 1
# rev = ""
# for i in a:
#     rev = i + rev
# if a == rev :
#     print("Palindrome")
    
# # approach 2
# left = 0 
# right = len(a) -1 
# palindrome = True
# while left <right :
#     if a[left] != a[right]:
#         palindrome = False
#         break
#     left +=1
#     right -=1
# if palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome ")


# # 3. Count Character Frequency  [Easy]
# # approach 1
# a = input("Enter a string:")
# b = input("Enter a letter:")
# count = 0
# for i in a:
#     if i == b:
#         count +=1
# print(count)
# #approach 2
# c = input()
# b ={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i] = 1
# print(b)


# # 4. First Non-Repeating Character  [Easy]
# a = input("Enter a sting:")
# b ={}
# for i in a:
#     if i in b:
#         b[i] +=1
#     else:
#         b[i] =1 
# for i in b:
#     if b[i] == 1:
#         print(i)
#         break
        
        
# # 5. Remove Duplicate Characters  [Easy]
# a = input("Enter a string :")
# b = ""
# for i in a:
#     if i not in b:
#         b += i
# print(b)
        
        
# # 6. Anagram Check  [Easy]
# a = input("Enter a sting:")
# b = input("Enter second string:")
# if len(a) == len(b):
#     for i in a:
#         if i in b:
#             break
#     print("anagram")
# else:
#     print("Not anagram")
    

# # 7. Longest Word  [Easy]
# a = input("Enter a sting:")
# b = ""
# c =""
# for i in a:
#     if i != " ":
#         b += c 
#     c +=i
# for i in b:
#     if len(c) > len(b):
#         b = c
# print(b)