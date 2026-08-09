import numpy as np

marks = np.array([58, 98, 68, 64, 86, 92])

print(marks > 80)
print(marks[marks > 80])
print(marks[marks >= 90])
print(marks[marks < 60])
print(marks[(marks >= 70) & (marks <= 90)])
print(marks[marks == 75])

above_80 = marks[marks > 80]
print(f"Students above 80: {above_80.size}")
print(f"Highest above 80: {np.max(above_80)}")

result = np.where(marks >= 75, "Pass", "Needs Improvement")
print(result)

grace_marks = np.where(marks < 60, marks + 5, marks)
print(grace_marks)

below_70 = marks[marks < 70]
print(below_70)
