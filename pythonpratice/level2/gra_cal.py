user_marks =int(input("Enter a your marks for english:"))

if 100 < user_marks >= 0 :
    print("Invaild Marks ")
else :
    if 90 <= user_marks <= 100 :
        print("A+")
    elif 80 <= user_marks <= 89:
        print("A")
    elif 79 <= user_marks <= 70:
        print("B")
    elif 69 <= user_marks <= 60:
        print("C")
    elif 59 <= user_marks <= 50:
        print("D")
    else:
        print("F")