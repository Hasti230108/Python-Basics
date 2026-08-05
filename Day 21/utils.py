import json

def menu():
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def load_students():
    with open("student.json", "r") as file:
        students = json.load(file)
    return students

def save_students(students):
    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)

