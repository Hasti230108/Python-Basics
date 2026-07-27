name = input("Enter your name: ")
rollno = int(input("Enter your roll number: "))
course = input("Enter your course: ")
semester = int(input("Enter your semester: "))
city = input("Enter your city: ")

file = open("student_record.txt", "a")

file.write(f"\nStudent Name: {name} \n")
file.write(f"Roll Number: {rollno} \n")
file.write(f"Course: {course} \n")
file.write(f"Semester: {semester} \n")
file.write(f"City: {city} \n")

file.close()

print("Record saved successfully!")

with open("student_record.txt", "r") as file:
    content = file.read()
    print("\nRecords: \n")
    print(content)

print("File is closed automatically.")