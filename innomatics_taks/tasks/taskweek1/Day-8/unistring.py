s = (input("Enter a String: "))
unique = ""
for i in s:
    if i not in unique:
        unique += i
print("The unique string is: ", unique)
    