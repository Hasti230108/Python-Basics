import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

print(f"Original: {numbers}")
print(f"Original shape: {numbers.shape}")

reshaped = numbers.reshape(2, 3)

print(f"\nReshaped:\n{reshaped}")
print(f"Reshaped shape: {reshaped.shape}")

print(f"Flattened: {reshaped.flatten()}")
print(f"Ravelled: {reshaped.ravel()}")

print(f"\nTranspose:\n{reshaped.T}")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"\nArray A: {a}")
print(f"Array B: {b}")

print(f"\nConcatenate: {np.concatenate((a, b))}")
print(f"Vertical stack:\n{np.vstack((a, b))}")
print(f"Horizontal stack: {np.hstack((a, b))}")

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print(f"\nMatrix A:\n{matrix_a}")
print(f"\nMatrix B:\n{matrix_b}")

print(f"\nVertical stack:\n{np.vstack((matrix_a, matrix_b))}")
print(f"\nHorizontal stack:\n{np.hstack((matrix_a, matrix_b))}")

print(f"\nCombined using concatenate:\n{np.concatenate((matrix_a, matrix_b), axis=0)}")
print(f"\nCombined by columns:\n{np.concatenate((matrix_a, matrix_b), axis=1)}")