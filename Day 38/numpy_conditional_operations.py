import numpy as np

marks = np.array([86, 94, 73, 46, 84, 61, 55, 84])

result = np.where(marks >= 50, "Pass", "Fail")

print("Marks:", marks)
print("Result:", result)

print(f"Marks above 80: {marks[marks >= 80]}")
print(f"Marks Between 50 and 80: {marks[(marks >= 50) & (marks <= 80)]}")

conditions = [
    marks >= 90,
    marks >= 70,
    marks >= 50,
    marks >= 40
]

choices = ["A", "B", "C", "D"]

grades = np.select(conditions, choices, default="F")

bonus = np.array([5, 0, 10, 5, 8, 0, 12, 3])

print(f"Marks capped at 100: {np.minimum(marks + bonus, 100)}")

clipped_marks = np.clip(marks, 40, 90)
print(f"Clipped Marks: {clipped_marks}")

print(f"Number of students who passed: {np.sum(marks >= 50)}")

print(f"Student scored more than 90: {np.any(marks >= 90)}")

print(f"Every student score at least 50: {np.all(marks >= 50)}")

adjusted_marks = marks.copy()
adjusted_marks[adjusted_marks < 50] = 50
print(f"Adjusted Marks: {adjusted_marks}")