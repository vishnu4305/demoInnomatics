import csv 
try: 
    file = open("employees_data.csv", "r") 
    reader = csv.reader(file) 
    header = next(reader) 

    new_sal = []

    for row in reader: 
        year = row[3].split("-")[0] 

        if year == "2024": 
            salary = float(row[2]) 
            salary = salary + (salary * 20 / 100) 
            row[2] = salary 
        new_sal.append(row) 
    file.close() 

    file = open("updated_employees.csv", "w", newline="") 
    writer = csv.writer(file) 
    writer.writerow(header) 
    writer.writerows(new_sal) 
    file.close() 
     
except FileNotFoundError: 
    print("employees_data.csv file not found.") 
except Exception as e: 
    print(f"Error: {e}")
else:
    print("Salary increment applied successfully.")
finally:
    print("Program run Successfully")