def Largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n>largest:
            largest =n

    return largest

def Smallest(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n<smallest:
            smallest =n

    return smallest

def Sum(numbers):
    total = 0
    for n in numbers:
        total = total + n

    return total

def Average(numbers, count):
    sum = 0
    for n in numbers:
        sum = sum + n
    
    average = sum / count
    return average

numbers_list = []

count = int(input("Enter a number: "))

for i in range(count):
    num = int(input(f"Enter a number {i + 1}: "))
    numbers_list.append(num)

numbers = tuple(numbers_list)

print("Tuple: ", numbers)
print("Largest number:", Largest(numbers))
print("Smallest number:", Smallest(numbers))
print("Sum:", Sum(numbers))
print("Average:", Average(numbers, count))