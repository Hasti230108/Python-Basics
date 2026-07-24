class Bird:
    def sound(self):
        print("Bird chirps.")

class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

animals = [Bird(), Dog(), Cat()]
for animal in animals:
    animal.sound()