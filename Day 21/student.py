from utils import *

while True:

    while True:
        try:
            menu()
            choice = int(input("\nEnter your choice: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if choice == 1:

        students = load_students()

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        roll_no = int(input("Enter Roll Number: "))
        course = input("Enter Course: ")
        city = input("Enter City: ")
        marks = int(input("Enter Marks: "))

        duplicate = False

        for student in students:
            if student["roll_no"] == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Roll Number already exists.")
            continue

        if marks >= 90:
            grade = "O"
            result = "passed"
        elif marks >= 80:
            grade = "A"
            result = "passed"
        elif marks >= 60:
            grade = "C"
            result = "passed"
        elif marks >= 40:
            grade = "D"
            result = "passed"
        else:
            grade = "F"
            result = "failed"

        students.append({
            "name": name,
            "age": age,
            "roll_no": roll_no,
            "course": course,
            "city": city,
            "marks": marks,
            "grade": grade,
            "result": result
        })

        save_students(students)

        print("\nStudent Added Successfully!")

    elif choice == 2:

        students = load_students()

        if len(students) == 0:
            print("\nNo Students Found.")

        else:
            print("\n--- Student Records ---")

            for student in students:

                print(f"""
Roll No : {student['roll_no']}
Name    : {student['name']}
Age     : {student['age']}
Course  : {student['course']}
City    : {student['city']}
Marks   : {student['marks']}
Grade   : {student['grade']}
Result  : {student['result']}
""")

    elif choice == 3:

        students = load_students()

        roll = int(input("Enter Roll Number to Update: "))

        found = False

        for student in students:

            if student["roll_no"] == roll:

                print("\nStudent Found!")

                student["name"] = input("Enter New Name: ")
                student["age"] = int(input("Enter New Age: "))
                student["course"] = input("Enter New Course: ")
                student["city"] = input("Enter New City: ")
                student["marks"] = int(input("Enter New Marks: "))

                if student["marks"] >= 90:
                    student["grade"] = "O"
                    student["result"] = "passed"
                elif student["marks"] >= 80:
                    student["grade"] = "A"
                    student["result"] = "passed"
                elif student["marks"] >= 60:
                    student["grade"] = "C"
                    student["result"] = "passed"
                elif student["marks"] >= 40:
                    student["grade"] = "D"
                    student["result"] = "passed"
                else:
                    student["grade"] = "F"
                    student["result"] = "failed"

                found = True
                break

        if found:
            save_students(students)
            print("Student Updated Successfully.")
        else:
            print("Student Not Found.")

    elif choice == 4:

        students = load_students()

        roll = int(input("Enter Roll Number to Delete: "))

        found = False

        for student in students:

            if student["roll_no"] == roll:
                students.remove(student)
                found = True
                break

        if found:
            save_students(students)
            print("Student Deleted Successfully.")
        else:
            print("Student Not Found.")

    elif choice == 5:
        print("\nThank You!")
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid Choice.")