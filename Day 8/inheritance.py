class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, {self.name}")

class Student(Person):
    def __init__(self, name, course="AI & ML"):
        super().__init__(name)
        self.course = course

    def display(self):
        print(f"{self.name} your course is {self.course}")

student1 = Student("Tinker")
student2 = Student("Daksh", "Data Science")

student1.greet()
student1.display()

student2.greet()
student2.display()