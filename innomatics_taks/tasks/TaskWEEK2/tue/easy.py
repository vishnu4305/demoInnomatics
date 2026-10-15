#6.	Print all multiples of 5 between 1 and 100.
print("-----------------------------")
print("-----------------------------")
print("Print all multiples of 5 between 1 and 100.")
print("-----------------------------")
for i in range(1,101):
    if i % 5 == 0 :
        print( i ,end= " ")
    
print()
    

#7.	Print the sum of numbers from 1 to 50.
print("-----------------------------")
print("-----------------------------")
print("Print the sum of numbers from 1 to 50.")
print("-----------------------------")
    
sum = 0    
for i in range(1,50):
    sum+=i
print(f"sum = {sum}")
    

#8.Count how many numbers are divisible by 3 from 1 to 100..
print("-----------------------------")
print("-----------------------------")
print("Count how many numbers are divisible by 3 from 1 to 100.")
print("-----------------------------")
count = 0
for i in range(1,101):
    if i % 3 == 0:
        count += 1
print(f"between 1 and 100, multiples of 3 count = {count}")

#9.	Print all characters of a string one by one.
print("-----------------------------")
print("-----------------------------")
print("Print all characters of a string one by one.")
print("-----------------------------")
str = input("Enter a string: ")
for i in str:
    print(i)
    
#10.	Print numbers from 1 to 100 except multiples of 4.
print("-----------------------------")
print("-----------------------------")
print("Print numbers from 1 to 100 except multiples of 4.")
print("-----------------------------")
for i in range(1,101):
    if i %  4 == 0:
        print(i , end =" ")
    


