import math

class Shape:
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of Rectangle: {self.length * self.breadth}") 

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of Square: {self.side * self.side}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle: {math.pi * self.radius * self.radius:.2f}")


SA = Square(8)
SA.area()
RA = Rectangle(6, 5)
RA.area()
CA = Circle(3)
CA.area()
