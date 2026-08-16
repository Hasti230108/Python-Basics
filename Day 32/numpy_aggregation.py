import numpy as np

marks = np.array([45, 78, 92, 47, 96, 87, 83, 79])

print(f"Original marks: {marks}")

# Basic aggregation
print(f"\nSum: {np.sum(marks)}")
print(f"Mean: {np.mean(marks)}")
print(f"Median: {np.median(marks)}")
print(f"Maximum: {np.max(marks)}")
print(f"Minimum: {np.min(marks)}")

# Statistics
print(f"\nStandard deviation: {np.std(marks)}")
print(f"Variance: {np.var(marks)}")

# Range
print(f"Range: {np.max(marks) - np.min(marks)}")

# Count
print(f"\nTotal students: {marks.size}")
print(f"Passed students: {np.count_nonzero(marks >= 40)}")
print(f"Students above 80: {np.count_nonzero(marks > 80)}")

# 2D array
matrix = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 88]
])

print(f"\nMarks Matrix:\n{matrix}")

# Entire matrix
print(f"\nMatrix sum: {np.sum(matrix)}")
print(f"Matrix mean: {np.mean(matrix)}")
print(f"Matrix maximum: {np.max(matrix)}")
print(f"Matrix minimum: {np.min(matrix)}")

# Axis operations
print(f"\nRow totals: {np.sum(matrix, axis=1)}")
print(f"Column totals: {np.sum(matrix, axis=0)}")

print(f"Row averages: {np.mean(matrix, axis=1)}")
print(f"Column averages: {np.mean(matrix, axis=0)}")

print(f"Row maximums: {np.max(matrix, axis=1)}")
print(f"Column maximums: {np.max(matrix, axis=0)}")

print(f"Row minimums: {np.min(matrix, axis=1)}")
print(f"Column minimums: {np.min(matrix, axis=0)}")

# Cumulative operations
print(f"\nCumulative sum: {np.cumsum(marks)}")
print(f"Cumulative product: {np.cumprod(marks)}")