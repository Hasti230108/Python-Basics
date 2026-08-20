import numpy as np

matrix = np.array([
    [1, 2],
    [3, 4]
])

print(f"Original matrix:\n{matrix}")

print(f"\nDeterminant of matrix: {np.linalg.det(matrix):.1f}")

print(f"\nInverse of matrix:\n{np.linalg.inv(matrix)}")

print(f"\nRank of matrix: {np.linalg.matrix_rank(matrix)}")

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([5, 11])
solution = np.linalg.solve(a, b)

print(f"\nSolution of equations: {solution}")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print(f"\nEigenvalues: {eigenvalues}")
print(f"\nEigenvectors:\n{eigenvectors}")