class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

s_name = input("Enter name of Student: ")
s_age = int(input("Enter age of Student: "))
s_course = input("Enter course of Student: ")

student1 = Student(s_name, s_age, s_course)

student1.display()