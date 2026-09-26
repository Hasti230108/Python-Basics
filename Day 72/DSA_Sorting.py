length = int(input("Enter the number of length of list: "))

numbers = []

for i in range(length):
    number = int(input(f"Enter {i + 1} number: "))
    numbers.append(number)

print("\nOriginal List:", numbers)

# Insertion Sort

for i in range(1, length):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = key

print("Ascending Sorted List:", numbers)

# Insertion Sort - Descending

for i in range(1, length):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] < key:
        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = key

print("Descending Sorted List:", numbers)