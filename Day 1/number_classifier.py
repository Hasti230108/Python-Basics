print("To check whether the given number is positive/negative or even/odd")
num = int(input("Enter number:"))

if num % 2 == 0 and num > 0:
    print("Positive Even Number")
elif num % 2 == 1 and num > 0:
    print("Positive Odd Number")
elif num % 2 == 0 and num < 0:
    print("Negative Even Number")
elif num % 2 == 1 and num < 0:
    print("Negative Odd Number")
else:
    print("Zero")