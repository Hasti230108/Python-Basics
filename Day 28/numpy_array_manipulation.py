import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print(f"Original: {numbers}")
print(f"Shape: {numbers.shape}")
print(f"Dimensions: {numbers.ndim}")
print(f"Size: {numbers.size}")

matrix = numbers.reshape(2, 3)

print(f"\nReshaped:\n{matrix}")
print(f"Shape: {matrix.shape}")
print(f"Dimensions: {matrix.ndim}")

print(f"\nRavel: {matrix.ravel()}")
print(f"Flatten: {matrix.flatten()}")

print(f"\nTranspose:\n{matrix.T}")

marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 88]
])

print(f"\nMarks:\n{marks}")
print(f"Row totals: {np.sum(marks, axis=1)}")
print(f"Column totals: {np.sum(marks, axis=0)}")
print(f"Row averages: {np.mean(marks, axis=1)}")
print(f"Column averages: {np.mean(marks, axis=0)}")