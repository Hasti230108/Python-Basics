def divide_numbers():
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))

        result = num1/num2

    except ValueError:
        print("Error: Please enter valid numeric values")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

    else:
        print("Division successful. Result:", result)

    finally:
        print("Execution complete.")

divide_numbers()
