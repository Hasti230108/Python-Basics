from utils import generate_account_number

def createNewAccount():
    name = input("Enter your name:")
    while(1):
        try:
            age = int(input("Enter your age:"))
            if age < 18:
                print("You must be at least 18 years old to create an account.")
                return
            break
        except ValueError:
            print("Invalid age. Please enter a valid age.")
    while(1):
        phone = input("Enter your phone number:")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid phone number. Please enter a valid 10-digit phone number.")
    while(1):
        email = input("Enter your email address:")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email address. Please enter a valid email address.")

    while True:
        try:
            balance = float(input("Enter initial deposit:"))
            break
        except ValueError:
            print("Invalid amount. Please enter a valid amount.")

    account_number = generate_account_number()

    with open("accounts.txt", "a") as file:
        file.write(f"Account Number: {account_number}, Name: {name}, Age: {age}, Phone: {phone}, Email: {email}, Balance: {balance}\n")

    print(f"Account created successfully! Your account number is: {account_number}")


def login():
    account_number = input("Enter your account number:").upper()
    with open("accounts.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")

            if data[0] == f"Account Number: {account_number}":
                print("Login successful!")
                return data

    print("Account not found. Please check your account number or create a new account.")
    return None

def show_account_details(account_data):
    print("\n===== Account Details =====\n")
    for item in account_data:
        print(item)

def check_balance(account_data):
    balance = float(account_data[5].split(": ")[1])
    print(f"Your current balance is: {balance}")

def deposit(account_data):
    while(1):
        try:
            amount = float(input("Enter the amount to deposit:"))
            if amount < 0:
                print("Invalid amount.")
                continue
            else:
                account_data[5] = f"Balance: {float(account_data[5].split(': ')[1]) + amount}"
                update_account(account_data)
                print(f"Deposited {amount} successfully.")
                break
        except ValueError:
            print("Invalid amount. Please enter a valid amount.")

def withdraw(account_data):
    while(1):
        try:
            amount = float(input("Enter the amount to withdraw:"))
            current_balance = float(account_data[5].split(": ")[1])
            if amount < 0:
                print("Invalid amount.")
                continue
            elif amount > current_balance:
                print("Insufficient balance.")
                continue
            else:
                account_data[5] = f"Balance: {current_balance - amount}"
                update_account(account_data)
                print(f"Withdrew {amount} successfully.")
                break
        except ValueError:
            print("Invalid amount. Please enter a valid amount.")

def update_account(account_data):
    with open("accounts.txt", "r") as file:
        lines = file.readlines()

    with open("accounts.txt", "w") as file:
        for line in lines:
            if line.startswith(f"Account Number: {account_data[0].split(': ')[1]}"):
                file.write(", ".join(account_data) + "\n")
            else:
                file.write(line)