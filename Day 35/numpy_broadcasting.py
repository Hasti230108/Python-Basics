import numpy as np

numbers = np.array([10, 20, 30, 40])

print(f"Original: {numbers}")

print(f"\nAdd 10: {numbers + 10}")
print(f"Subtract 5: {numbers - 5}")
print(f"Multiply by 2: {numbers * 2}")
print(f"Divide by 10: {numbers / 10}")

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(f"\nMatrix:\n{matrix}")

print(f"\nAdd 10 to matrix:\n{matrix + 10}")

row = np.array([1, 2, 3])

print(f"\nRow: {row}")
print(f"\nMatrix + Row:\n{matrix + row}")

column = np.array([
    [1],
    [2],
    [3]
])

print(f"\nColumn:\n{column}")
print(f"\nMatrix + Column:\n{matrix + column}")

print(f"\nMatrix * 2:\n{matrix * 2}")

marks = np.array([
    [45, 60, 75],
    [68, 86, 73],
    [96, 84, 62]
])

bonus = np.array([5, 10, 5])

print(f"\nMarks:\n{marks}")
print(f"\nBonus:\n{bonus}")

print(f"\nMarks after bonus:\n{marks + bonus}")

print(f"\nMarks capped at 100:\n{np.minimum(marks + bonus, 100)}")
