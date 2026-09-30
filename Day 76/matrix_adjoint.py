import numpy as np

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []

    for j in range(columns):
        number = int(input(f"Enter element [{i}][{j}]: "))
        row.append(number)

    matrix.append(row)

matrix = np.array(matrix)

print("\nOriginal Matrix:")
print(matrix)

if rows == 2 and columns == 2:

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    adjoint = np.array([
        [d, -b],
        [-c, a]
    ])

    print("\nAdjoint Matrix:")
    print(adjoint)

elif rows == 3 and columns == 3:

    cofactor_matrix = np.zeros((3, 3), dtype=int)

    for i in range(3):
        for j in range(3):

            minor = np.delete(
                np.delete(matrix, i, axis=0),
                j,
                axis=1
            )

            determinant = (
                minor[0][0] * minor[1][1]
                - minor[0][1] * minor[1][0]
            )

            cofactor_matrix[i][j] = ((-1) ** (i + j)) * determinant

    print("\nCofactor Matrix:")
    print(cofactor_matrix)

    adjoint = cofactor_matrix.T

    print("\nAdjoint Matrix:")
    print(adjoint)

else:
    print("\nAdjoint is currently implemented for 2x2 and 3x3 matrices only.")