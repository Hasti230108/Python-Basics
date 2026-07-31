try :
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operator = input("Enter an operator (+ - * /): ")

    if operator == '+':
        addition = num1+num2
        print(f"Addition: {addition}")

    elif operator == '*':
        multiplication = num1*num2
        print(f"Multiplication: {multiplication}")

    elif operator == '-':    
        subtraction = num1-num2
        print(f"Subtraction: {subtraction}")

    elif operator == '/':
        division = num1/num2
        print(f"Division: {division}")
        
    else:
        print("Wrong operator enter.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
