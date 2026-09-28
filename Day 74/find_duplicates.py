length = int(input("Enter the number of length of list: "))

numbers = []

for i in range(length):
    number = int(input(f"Enter {i + 1} number: "))
    numbers.append(number)

print("\nOriginal List:", numbers)

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("\nDuplicate Elements:")

found = False

for number in frequency:
    if frequency[number] > 1:
        print(number, "appears", frequency[number], "times")
        found = True

if not found:
    print("No duplicate elements found.")