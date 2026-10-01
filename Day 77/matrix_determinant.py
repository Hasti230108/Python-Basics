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

    determinant = (a * d) - (b * c)

    print("\nDeterminant:", determinant)

else:
    print("\nDeterminant is currently implemented for 2x2 matrices only.")
    