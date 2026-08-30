student_names = ["Aarav", "Bhavna", "Chetan", "Diyya", "Esha"]
student_marks = [45, 88, 92, 35, 75]
noofstu = len(student_names)
average_mark = 0
average_sum =0
count_pass = 0
count_fail = 0
highest_marks = 0
topper_name = " "

print(f"Total number of students in the class :{noofstu}")

for i in range(noofstu):
    if student_marks[i] >= 80:
        print(f"{i+1} . {student_names[i]} : {student_marks[i]} Grade A (Pass)")
        count_pass += 1
    elif 79 <= student_marks[i] >= 50:
        print(f"{i+1} . {student_names[i]} : {student_marks[i]} Grade B (Pass)")
        count_pass += 1
    else:
        print(f"{i+1} . {student_names[i]} : {student_marks[i]} Grade F (Fail)")
        count_fail += 1
    average_sum =average_sum + student_marks[i]
    
    if student_marks[i] > highest_marks:
        topper_name = student_names[i]
        highest_marks =student_marks[i] 
print(f"Topper of the Class : {topper_name} - {highest_marks}")
print(f"Total sum of marks :{average_sum}") 

average_mark = average_sum / noofstu
print(f"Average Mark of class : {average_mark}")
print(f"No of Students Pass: {count_pass}")
print(f"No of Students Fail: {count_fail}")