user_num = input("Enter a number :")
largest = 0
for num in user_num:
    if int(num) > largest:
        largest = int(num)
print(f"Largest digit in the number: {largest}") 