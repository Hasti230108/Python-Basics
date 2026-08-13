import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print(f"Original: {numbers}")
print(f"First three: {numbers[:3]}")
print(f"Last three: {numbers[-3:]}")
print(f"Middle: {numbers[2:5]}")
print(f"Every second: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(f"\nMatrix:\n{matrix}")
print(f"First row: {matrix[0]}")
print(f"Second column:{matrix[:, 1]}")
print(f"First two rows: \n{matrix[:2]}")
print(f"Last two columns: \n{matrix[:, 1:]}")
print(f"Middle value: {matrix[1,1]}")

view = numbers[1:4]
view[0] = 999

print(f"\nAfter changing view: {numbers}")

copy = numbers[1:4].copy()
copy[0] = 111

print(f"After changing copy: {numbers}")
print(f"Copy: {copy}")

print(f"\nPractice:")
print(f"First four: {numbers[:4]}")
print(f"Odd positions: {numbers[::2]}")
print(f"Last column: {matrix[:, -1]}")