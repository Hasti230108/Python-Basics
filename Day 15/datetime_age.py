from datetime import datetime

birth = int(input("Enter birth year: "))

current = datetime.now().year

print(f"Age: {current-birth}")