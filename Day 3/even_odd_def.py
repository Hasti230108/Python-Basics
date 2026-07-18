def Number(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number:"))

if Number(num):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
