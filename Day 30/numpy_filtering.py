import numpy as np

marks = np.array([45, 78, 92, 47, 96, 87, 83, 79])

print(f"Original: {marks}")

print(f"Above 80: {marks[marks > 80]}")
print(f"Positions above 80: {np.where(marks > 80)}")
print(f"\nBelow 60: {marks[marks < 60]}")
print(f"Positions below 60: {np.where(marks < 60)}")
print(f"\nMarks Between 60 and 80: {marks[(marks >= 60) & (marks <= 80)]}")

print(f"\nPassed marks: {marks[marks >= 40]}")
print(f"Failed marks: {marks[marks < 40]}")

print(f"\nUsing logical_and: {marks[np.logical_and(marks >= 60, marks <= 80)]}")
print(f"Using logical_or: {marks[np.logical_or(marks < 50, marks > 90)]}")