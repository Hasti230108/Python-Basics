class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Tinker", 18, "AI & ML")
student2 = Student("Twinkle", 19, "Data Science")

print(f"Name of Student 1: {student1.name}")
print(f"Course of Student 2: {student2.course}")