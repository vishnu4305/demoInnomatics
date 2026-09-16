user_str = input("Enter an string :")
count = 0
vowels = "aeiouAEIOU"
for ch in user_str:
    if ch in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")
