def add_record():
    file = open("students.txt", "a")
    name = input("Enter student name: ")
    rollnumber = int(input("Enter roll number: "))
    course = input("Enter course: ")
    file.write(f"{name}, {rollnumber}, {course}\n")
    file.close()

def display_records():
    with open("students.txt", "r") as file:
        print("Student Records:")
        for line in file:
            print(line.strip())

def search_records():
    rollnumber = int(input("Enter roll number to search: "))
    with open("students.txt", "r") as file:
        found = False
        for line in file:
            name, roll, course = line.strip().split(", ")
            if int(roll) == rollnumber:
                print(f"Record found: Name: {name}, Roll Number: {roll}, Course: {course}")
                found = True
                break
        if not found:
            print("Record not found.")

def delete_record():
    rollnumber = int(input("Enter roll number to delete: "))
    with open("students.txt", "r") as file:
        lines = file.readlines()

    with open("students.txt", "w") as file:
        found = False
        for line in lines:
            name, roll, course = line.strip().split(", ")
            if int(roll) != rollnumber:
                file.write(line)
            else:
                found = True

    if found:
        print(f"Record deleted successfully.")
    else:
        print("Record not found.")