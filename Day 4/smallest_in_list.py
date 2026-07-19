def Smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

count = int(input("How many numbers do you want to enter?: "))
numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("The numbers you entered are:", numbers)
print("The smallest number is:", Smallest(numbers))