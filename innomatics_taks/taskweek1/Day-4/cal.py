a = int(input("Enter first value :"))
b = int(input("Enter second value :"))
operation = input(""" Enter One of Opertion
                  ----------------
                  List of operations:
                  ----------------
                  1. +  
                  2. - 
                  3. * 
                  4. /
                  5. %
                  6.**
                  ----------------
                  """)
if operation == "+":
    print(f"a+b = {a+b}")
elif operation == "-":
    print(f"a-b = {a-b}")
elif operation == "-":
    print(f"a*b = {a*b}")
elif operation == "-":
    print(f"a/b = {a/b}")
elif operation == "-":
    print(f"a%b = {a%b}")
elif operation == "-":
    print(f"a**b = {a**b}")
else:
    print("operation is not avaiable")
    