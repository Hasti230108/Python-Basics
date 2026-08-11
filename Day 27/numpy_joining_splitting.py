import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

print(f"Array A: {a}")
print(f"Array B: {b}")

print(f"Concatenate: {np.concatenate((a,b))}")
print(f"Vertiacl Stack: \n{np.vstack((a,b))}")
print(f"Horizontal Stack: {np.hstack((a,b))}")
print(f"Stack: \n{np.stack((a,b))}")

numbers = np.array([10, 20, 30, 40, 50, 60])
print(f"Split: {np.split(numbers, 3)}")

marks = np.array([[80, 85, 91],
                  [70, 75, 80],
                  [90, 95, 88],
                  [60, 65, 70]])
print(f"Marks: \n{marks}")
print(f"Vertical split: \n{np.vsplit(marks, 2)}")
print(f"Horizontal split: \n{np.hsplit(marks, 3)}")

marks_sem1 = np.array([[80, 85, 91],
                       [70, 75, 80],
                       [90, 95, 88],
                       [60, 65, 70]])
mark_sem2 = np.array([[95, 75, 88],
                      [61, 86, 76],
                      [98, 68, 84],
                      [88, 87, 79]])

print(f"Concatenate: \n{np.concatenate((marks_sem1, mark_sem2), axis=1)}")