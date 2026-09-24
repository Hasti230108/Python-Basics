length = int(input("Enter the number of length of list: "))

numbers = []

for i in range(length):
    number = int(input(f"Enter {i + 1} number: "))
    numbers.append(number)

print("\nOriginal List:", numbers)

# Selection Sort

for i in range(length):
    min_index = i

    for j in range(i+1, length):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Ascending Sorted List:", numbers)

for i in range(length):
    min_index = i

    for j in range(i+1, length):
        if numbers[j] > numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Descending Sorted List:", numbers)