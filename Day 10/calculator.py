try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(f"Answer: {num1 + num2}")
    elif operator == "-":
        print(f"Answer: {num1 - num2}")
    elif operator == "*":
        print(f"Answer: {num1 * num2}")
    elif operator == "/":
        print(f"Answer: {num1 / num2}")
    else:
        print("Invalid operator.")

except ValueError:
    print("Enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")