length = int(input("Enter the number of length of list: "))

numbers = []

for i in range(length):
    number = int(input(f"Enter {i + 1} number: "))
    numbers.append(number)

print("\nOriginal List:", numbers)

# Bubble Sort

for i in range(length):
    for j in range(0, length - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Ascending Sorted List:", numbers)

for i in range(length):
    for j in range(0, length - i - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Descending Sorted List:", numbers)