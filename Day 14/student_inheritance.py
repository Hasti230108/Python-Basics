class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_Person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no, course, semester):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
        self.semester = semester

    def display_Student(self):
        self.display_Person()
        print(f"Roll No.: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"Semester: {self.semester}")

name = input("Enter your name: ")
age = input("Enter your age: ")
stud = input("Are you Student? (yes or no): ")
stud = stud.lower()
if stud == "yes":
    roll_no = input("Enter Roll no: ")
    course = input("Enter Course: ")
    semester = input("Enter Semester: ")
    student_detail = Student(name, age, roll_no, course, semester)
    print("---DETAILS---")
    student_detail.display_Student()
elif stud == "no":
    print("---Person's Deatil---")
    person_detail = Person(name, age)
    person_detail.display_Person()
    print("Not a student.")
else:
    print("Entered Wrong Detail.")