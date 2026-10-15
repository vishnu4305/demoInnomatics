# # Print All Prime Numbers from m to n
# m = 10
# n = 30
# for num in range(m, n + 1):
#     if num < 2:
#         continue
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num, end=" ")

# # Count All Prime Numbers from m to n
# m = 1
# n = 10
# prime_count = 0
# for num in range(m, n + 1):
#     if num < 2:
#         continue
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         prime_count += 1
# print("Prime count:", prime_count)

# # Print All Armstrong Numbers in a Range
# m = 1
# n = 500
# for num in range(m, n + 1):
#     temp = num
#     digits = 0
#     while temp > 0:
#         digits += 1
#         temp //= 10
#     temp = num
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp //= 10
#     if total == num:
#          print(num, end=" ")

# # First Prime Number from m to n
# m = 10
# n = 25
# for num in range(m, n + 1):
#     if num < 2:
#         continue
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print("First prime:", num)
#         break

# # Last Prime Number from m to n
# m = 10
# n = 25
# last_prime = 0
# for num in range(m, n + 1):
#     if num < 2:
#         continue
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         last_prime = num
# print("Last prime:", last_prime)

# # 6. First Vowel in a Name
# name = "Vishnu"
# for char in name:
#     if char in "aeiouAEIOU":
#         print("First vowel:", char)
#         break

# # Last Vowel in a Name
# name = "vishnu"
# last=""
# for char in name:
#     if char in "aeiouAEIOU":
#         last= char
# print("Last vowel:", last)


# # Print All Even Numbers Using continue
# n = 10
# for num in range(1, n + 1):
#     if num % 2 != 0:
#         continue
#     print(num, end=" ")

# # Print All Odd Numbers Using continue
# n = 10
# for num in range(1, n + 1):
#     if num % 2 == 0:
#         continue
#     print(num, end=" ")

# Count Prime and Composite Numbers from m to n
m = 1
n = 10
prime_count = 0
composite_count = 0
for num in range(m, n + 1):
    if num < 2:
        continue
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        prime_count += 1
    else:
        composite_count += 1
print("Prime:", prime_count)
print("Composite:", composite_count)