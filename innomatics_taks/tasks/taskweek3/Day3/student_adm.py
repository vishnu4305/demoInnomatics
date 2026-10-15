Pre_data = [(1,"vishnu",100),
            (2,"vamsi",90),
            (3,"vis",80),
            (1,"vishnu",100)]
student = set()

seen_roll_numbers = set()
clean_students =[]


total =0
top_student = None

for data in Pre_data:
    Roll_No , Name ,Marks = data
    if Roll_No not in seen_roll_numbers:
        seen_roll_numbers.add(Roll_No)
        clean_students.append(data)
        
        total+=Marks
        
        if top_student is None or Marks > top_student[2]:
            top_student = data

average_marks = total / len(clean_students)

print("=" * 30)
print("           UNIQUE STUDENT RECORDS")
print("=" * 30)

print(f"Roll No   |  Name     | Marks ")
print("-" * 30)

for roll_no, name, marks in clean_students:
    print(f"{roll_no}  .{name }      :{marks}")

print("-" * 30)

print(f"Total Unique Students : {len(clean_students)}")
print(f"Average Marks         : {average_marks}")

print("\nTop Scorer Details")
print(f"Roll No               : {top_student[0]}")
print(f"Name                  : {top_student[1]}")
print(f"Marks                 : {top_student[2]}")

print("=" * 30)