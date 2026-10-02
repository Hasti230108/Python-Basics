import numpy as np
A = np.array([
[4, 1],
[2, 3]
])
print("Matrix A:")
print(A)
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
# Verification
for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]
    print("\nEigenvalue:", eigenvalue)
    print("Eigenvector:", eigenvector)
    print("A × v:")
    print(A @ eigenvector)
    print("λ × v:")
    print(eigenvalue * eigenvector)
