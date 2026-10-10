operator = input("Enter the operator (+,-,*,/):")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if operator == "+":
    print("Result:", a+b)
elif operator == "-":
    print("Result:", a-b)
elif operator == "*":
    print("Result:", a*b)
elif operator == "/":
    if b == 0:
        print(a, "can't be divided by zero.")
    else:
        print("Result:", a/b)
else:
    print("Invalid operator")
