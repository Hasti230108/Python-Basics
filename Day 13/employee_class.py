class Employee:
    def __init__(self, emp_id, emp_name, dept, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.dept = dept
        self.salary = salary

    def display(self):
        print(f"\nEmployee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Department: {self.dept}")
        print(f"Salary: {self.salary}")

        if self.salary >= 50000:
            print("Salary Status: High Salary")
        elif self.salary >= 30000:
            print("Salary Status: Medium Salary")
        else:
            print("Salary Status: Low Salary")

for i in range(3):
    e_id = int(input(f"\nEnter employee {i+1} id:"))
    e_name = input(f"Enter employee {i+1} name: ")
    department = input(f"Enter employee {i+1} department: ")
    sal = int(input(f"Enter employee {i+1} salary: "))

    emp = Employee(e_id, e_name, department, sal)
    print(f"\n---Employee {i+1} details---")
    emp.display()