import random

students = []

n =int(input("Enter number of students: "))
for i in range(n):
    students.append(input(f"Enter Student {i+1}: "))

winner = random.choice(students)

print("Winner is:", winner)