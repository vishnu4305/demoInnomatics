#11.	Questions the user for a password until they enter "admin".
print("-----------------------------")
print("-----------------------------")
str = "admin"
while True:
    user = input("Enter string: ")
    if user == str:
        print("Correct string")
        break


#12.	Print numbers from 1 to 100 and stop at 57.
print("-----------------------------")
print("-----------------------------")
for i in range(1,101):
    if i == 57:
        break
    print(i , end= " ")
print()

#13.Count how many vowels are present in a string. – if ch in ‘aeiou’
print("-----------------------------")
print("-----------------------------")
count = 0
ch = "aeiou" or "AEIOU"
for i in str:
    if i in ch:
        count += 1
print(f"Total vowels in the string = {count}")

#14.	Find the largest digit in a number. – Take the number in string format – 123
print("-----------------------------")
print("-----------------------------")
user_num = input("Enter a number :")
largest = 0
for num in user_num:
    if int(num) > largest:
        largest = int(num)
print(f"Largest digit in the number: {largest}") 

#15.	Reverse a string using a loop.
print("-----------------------------")
print("-----------------------------")
rev = ""
for ch in str:
    rev = ch + rev
print(f"Reversed string: {rev}")