user_name = input("Enter your name:")
user_py_m =int(input("Enter your Python marks:"))
user_sql_m =int(input("Enter your SQl marks:"))
user_html_m =int(input("Enter your HTML marks:"))

total_marks = user_html_m+user_py_m+user_sql_m
Average = total_marks/3
print(f"""
      =========================================
                Student Result
      =========================================
      Student Name  :{user_name}
      Python Marks  : {user_py_m}
      SQL Marks     : {user_sql_m}
      HTML Marks    :{user_html_m}
      Average Marks :{Average}
      Total Marks   :{total_marks}
      Student PASS/Fail :
      """)
if Average >= 50 :
    print("Student PASS")
    if Average >=90:
        print("A+ Grade")
    elif Average >= 80:
        print("A Grade")
    elif Average >= 70:
        print("b Grade")
    elif Average >= 60:
        print("C Grade")
    else :
        print("D Grade")
    
else:
    print("Student Fail")
    print("F Grade")
    
