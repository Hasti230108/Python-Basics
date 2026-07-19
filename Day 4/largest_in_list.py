def Largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

count = int(input("How many numbers do you want to enter?: "))
numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("The numbers you entered are:", numbers)
print("The largest number is:", Largest(numbers))