try :
    number = int(input("Enter a number: "))
    result = 100/number
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter a valid integer.")