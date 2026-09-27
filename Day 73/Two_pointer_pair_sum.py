length = int(input("Enter the number of length of list: "))

numbers = []

for i in range(length):
    number = int(input(f"Enter {i + 1} number: "))
    numbers.append(number)

print("\nOriginal List:", numbers)

numbers.sort()

print("Sorted List:", numbers)

target = int(input("Enter target sum: "))

left = 0
right = len(numbers) - 1

found = False

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print(
            "Pair found:",
            numbers[left],
            "+",
            numbers[right],
            "=",
            target
        )
        found = True
        break

    elif current_sum < target:
        left = left + 1

    else:
        right = right - 1

if not found:
    print("No pair found.")