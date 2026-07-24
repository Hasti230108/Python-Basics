class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def getdetails(self):
        print("\n--Details--")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

student = Student(name, age, course)
student.getdetails()