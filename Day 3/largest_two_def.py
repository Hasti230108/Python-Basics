def Largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Largest number is:", Largest(num1, num2))