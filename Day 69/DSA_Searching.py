import numpy as np

length = int(input("Enter the number of length of list: "))

numbers = []

for num in range(length):
    number = int(input(f"Enter {num+1} number: "))
    numbers.append(number)

target = int(input("\nEnter a number to search: "))

print("\n==== Linear search ====")
found = False
for num in range(length):
    if target == numbers[num]:
        print("\nFound at index:", num)
        found = True
        break

if not found:
    print("\nNumber not found.")


print("\n==== Binary search ====")
n = np.sort(numbers)
print("Sorted List:", n)
found = False
left = 0
right = len(n)-1
middle = (left + right) // 2

while left <= right:
    if n[middle] == target:
        found = True
        print("Number found at sorted index: ", middle)
        print("Number found at position:", middle + 1)
        break

    elif n[middle] > target:
        right = middle - 1
        middle = (left + right) // 2

    else:
        left = middle + 1
        middle = (left + right) // 2

if not found:
    print("Number not found.")