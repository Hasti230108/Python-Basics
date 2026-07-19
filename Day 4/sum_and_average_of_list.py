def Sum(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

def Average(numbers, count):
    total = 0

    for num in numbers:
        total = total + num

    return total / count

count = int(input("How many numbers do you want to enter?:"))
numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}:"))
    numbers.append(number)

print("The numbers you entered are:", numbers)
print("The sum of the numbers is:", Sum(numbers))
print("The average of the numbers is:", Average(numbers, count))
