class Student:
    def __init__(self):
        self.__marks = 95
    def get_marks(self):
        return self.__marks

student = Student()

print(student.get_marks())