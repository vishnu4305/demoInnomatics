# left 90angle triangle...
n=5
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()


print("============================")
# right 90angle triangle...
for row in range(n):
    for space in range(n-row-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()


print("============================")
#triangle

for row in range(n):
    for space in range(n-row-1):
        print(" ",end= " ")
    for col in range(2*row+1):
        print("*",end= " ")
    print()


print("=============================")


# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end=" ")
    print("*" * (2 * i - 1))

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end=" ")
    print("*" * (2 * i - 1))