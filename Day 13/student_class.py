class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def display(self):
        print(f"\nStudent name: {self.name}")
        print(f"Roll No.: {self.roll}")
        print(f"Course: {self.course}")

stud1 = Student("Himanshi Mehra", 31, "AI and ML")
stud1.display()

stud2 = Student("Arnav Singhania", 35, "Data Science")
stud2.display()