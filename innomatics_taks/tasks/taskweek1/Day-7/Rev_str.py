str = input("Enter a string: ")
for ch in range(len(str)-1, -1, -1):
    print(str[ch], end="")