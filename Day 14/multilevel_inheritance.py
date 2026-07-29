class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_Person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, dept, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.dept = dept 
        self.salary = salary

    def display_Employee(self):
        self.display_Person()
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.dept}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, dept, salary, team_size):
        super().__init__(name, age, emp_id, dept, salary)
        self.team_size = team_size

    def display_Manager(self):
        self.display_Employee()
        print(f"Team Size: {self.team_size}")

name = input("Enter your Name: ")
age = int(input("Enter your age: "))
emp = input("Are you Employee? (yes or no): ")
emp = emp.lower()
if emp == "yes":
    emp_id = int(input("Enter your Employe ID: "))
    dept = input("Enter your department: ")
    salary = int(input("Enter your salary: "))
    manager = input("Are you Manager? (yes or no): ")
    manager = manager.lower()
    if manager == "yes":
        team_size = int(input("Enter your team size: "))
        print("\n---Manager Details---")
        m = Manager(name, age, emp_id, dept, salary, team_size)
        m.display_Manager()
    elif manager == "no":
        print("\n---Employee Details---")
        e = Employee(name, age, emp_id, dept, salary)
        e.display_Employee()
    else:
        print("Wrong Detail Entered.")
elif emp == "no":
    print("\n---Person Details---")
    p = Person(name, age)
    p.display_Person()
else:
    print("Wrong Detail Entered.")