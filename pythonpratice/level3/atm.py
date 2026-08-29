balance = 10000

user_enter = int(input("Enter a withdrawal amount :"))
if user_enter <=0:
    print("Invaild amount ")
elif balance >= user_enter:
    if user_enter % 100 == 0: 
        balance-=user_enter
        print("Withdrawel successful")
        print("Current Balance after withdrawel :",balance)
    else:
        print("Enter amount in multiples of 100")
else:
    print("Insufficient balance ")