import numpy as np

# 1D Array
marks = np.array([58, 98, 68, 64, 86, 92])
print(marks)
print(f"Sum: {np.sum(marks)}")
print(f"Mean: {np.mean(marks)}")
print(f"Minimum: {np.min(marks)}")
print(f"Maximum: {np.max(marks)}")
print(f"Standard Deviation: {np.std(marks)}")

# 2D Array
marks = marks.reshape(2, 3)
print(marks)
print(f"Total: {np.sum(marks)}")
print(f"Average: {np.mean(marks)}")
print(f"Column totals: {np.sum(marks, axis=0)}")
print(f"Row totals: {np.sum(marks, axis=1)}")

# 2D Array - Student Marks
marks = np.array([75, 82, 91, 88, 76, 95, 92, 89, 84])
marks = marks.reshape(3, 3)
print(marks)
print(f"Total: {np.sum(marks)}")
print(f"AVerage: {np.mean(marks)}")
print(f"Highest Marks: {np.max(marks)}")
print(f"Lowest Marks: {np.min(marks)}")
print(f"Total marks of each student: {np.sum(marks, axis=1)}")
print(f"Average marks of each student: {np.mean(marks, axis=1)}")
print(f"Total marks of each subject: {np.sum(marks, axis=0)}")
print(f"Average marks of each subject: {np.mean(marks, axis=0)}")