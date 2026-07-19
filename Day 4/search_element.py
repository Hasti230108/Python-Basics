count = int(input("How many numbers do you want to enter?: "))
numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}:"))
    numbers.append(number)

search = int(input("Enter the number you want to search for: "))
found = False
position = 0

for num in numbers:
    position += 1
    if num == search:
        found = True
        break

if found:
    print(f"The number {search} is present at position {position}.")
else:
    print(f"The number {search} is not present in the list.")