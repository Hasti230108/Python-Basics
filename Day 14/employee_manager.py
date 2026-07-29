class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
    def display_e(self):
        print(f"\nEmployee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, emp_id, emp_name, salary, department, team_size):
        super().__init__(emp_id, emp_name, salary)
        self.department = department
        self.team_size = team_size

    def display_m(self):
        self.display_e()
        print(f"Department: {self.department}")
        print(f"Team size: {self.team_size}")

manager = Manager(12345, "Harry Potter", 75000, "Ai and Ml", 9)
manager.display_m()