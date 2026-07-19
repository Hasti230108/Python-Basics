def Sorting(numbers, count):
    for i in range(count - 1):
        for j in range(count - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers

count = int(input("How many numbers do you want to enter?: "))
numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}:"))
    numbers.append(number)

sorted_list = Sorting(numbers, count)

print("Sorted list:", sorted_list)
print("Second largest number:", sorted_list[count-2])