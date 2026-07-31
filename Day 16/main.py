from utils import welcome, menu
from atm import check_balance, deposit, withdraw

name, AccNo = welcome()
balance = 5670

while(1):

    menu()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("--- Account Details ---")
            print(f"Account Holder: {name}")
            print(f"Account Number: {AccNo}")

            check_balance(balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)

        elif choice == 3:
            balance = withdraw(balance)

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("You enter wrong choice.")

    except ValueError:
        print("Please enter a valid number.")