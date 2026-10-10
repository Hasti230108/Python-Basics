class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_person(self):
        print("\nName:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def show_employee(self):
        self.show_person()
        print(f"Salary: {self.salary}")

name = input("Enter your name:")
age = int(input("Enter your age:"))
salary = float(input("Enter your salary:"))
e1 = Employee(name, age, salary)
e1.show_employee()
