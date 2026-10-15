num = int(input("Enter a number: "))
factor = 0
i =1
while i <= num+1:
    if num % i == 0:
        factor += 1
    i += 1
if factor == 2:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")