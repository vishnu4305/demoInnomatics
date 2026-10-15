#1.	Print numbers from 1 to 20.
print("-----------------------------")
print("Print numbers from 1 to 20")
print("-----------------------------")
for i in range(1,21):
    
    print(i ,end=" ")
print()
    
#2.	Print numbers from 20 to 1.
print("-----------------------------")
print("Print numbers from 20 to 1")
print("-----------------------------")  
for i in range(20,0,-1):
    print(i ,end=" ")
print()

#3.	Print all even numbers from 1 to 50.
print("-----------------------------")
print("Print all even numbers from 1 to 50")
print("-----------------------------")
for i in range(1,51):
    if i % 2 == 0:
        print(i , end=" ")
print()

#4.	Print all odd numbers from 1 to 50.
print("-----------------------------")
print("Print all odd numbers from 1 to 50")
print("-----------------------------")
for i in range(1,51):
    if i % 2 != 0:
        print(i , end=" ")
print() 

#5.	Print the multiplication table of 7.
print("-----------------------------")
print("Print the multiplication table of 7")
print("-----------------------------")
num = int(input("Enter a number: "))
for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
