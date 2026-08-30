emp_name = input("Enter your name:")
emp_sal =int(input("Enter your Salary:"))
emp_y_e =int(input("Enter your Years of Experience:"))
bonus = 0
if emp_y_e >= 10:
    print("Added 20% Bonus")
    bonus = emp_sal * (20/100) # 20% bonus 
elif emp_y_e >= 5:
    print("Added 10% Bonus")
    bonus = emp_sal * (10/100) # 10% bonus
elif emp_y_e >=2:
    print("Added 5% Bonus")
    bonus = emp_sal * (5/100) # 5% bonus
else:
    print("No Bonus")
final_sal = emp_sal+bonus
print(f"""
==============================
       EMPLOYEE PAYSLIP
==============================
Name        :{emp_name}
Basic Salary:{emp_sal}
Experience  :{emp_y_e}
Bonus       :{bonus}
Final Salary:{final_sal}
==============================
""")