import numpy as np

marks = np.array([
    [58, 98, 68],
    [64, 86, 92]
])

print(f"Dimensions: {marks.ndim}")
print(f"Shape: {marks.shape}")
print(f"Size: {marks.size}")
print(f"Marks of student 1: {marks[0]}")
print(f"Subject 3 marks of student 2: {marks[1][2]}")

zeros = np.zeros((2,4))
print(zeros)

ones = np.ones((2,4))
print(ones)

full = np.full((2,4), 9)
print(full)

arrange = np.arange(6, 23, 5)
print(arrange)

arrange = np.arange(63, 22, -4)
print(arrange)

line = np.linspace(0, 10, 6)
print(line)

line = np.linspace(1, 5, 5)
print(line)

array = np.array([1, 2, 3, 4, 5, 6])
new_array = array.reshape(2, 3)
print(new_array)
print(new_array.shape)

array = np.arange(1, 13)
new_array = array.reshape(3, 4)
print(new_array)