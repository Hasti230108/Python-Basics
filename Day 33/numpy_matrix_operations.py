import numpy as np

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print(f"Matrix A:\n{matrix_a}")
print(f"\nMatrix B:\n{matrix_b}")

print(f"\nElement-wise addition:\n{matrix_a + matrix_b}")
print(f"\nElement-wise subtraction:\n{matrix_a - matrix_b}")
print(f"\nElement-wise multiplication:\n{matrix_a * matrix_b}")

print(f"\nDot Product:\n{np.dot(matrix_a, matrix_b)}")

print(f"\nMatrix Multiplication using matmul:\n{np.matmul(matrix_a, matrix_b)}")

print(f"\nMatrix multiplication using @:\n{matrix_a @ matrix_b}")

print(f"\nTranspose of A:\n{matrix_a.T}")
print(f"\nTranspose of B:\n{matrix_b.T}")

print(f"\nDiagonal of A: {np.diag(matrix_a)}")
print(f"\nDiagonal of B: {np.diag(matrix_b)}")

print(f"\nTrace of A: {np.trace(matrix_a)}")
print(f"\nTrace of B: {np.trace(matrix_b)}")