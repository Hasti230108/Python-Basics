import random

def welcome():
    print("==== BANK MANAGEMENT SYSTEM ====")

def menu():
    print("\n1. Create New Account")
    print("2. Login")
    print("3. Exit")

def account_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Account Details")
    print("5. Logout")

def generate_account_number():
    while(1):
        number = random.randint(100000, 999999)

        found = 0
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    if f"Account Number: ACC{number}" in line:
                        found = 1
                        break
        except FileNotFoundError:
            return f"ACC{number}"

        if not found:
            return f"ACC{number}"