print("To check you are eligible for voting.")

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise Exception("You are not eligible.")

    print("Access Granted.")

except Exception as e:
    print(e)