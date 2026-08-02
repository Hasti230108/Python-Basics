from utils import *
from bank import *

welcome()

while(1):
    menu()
    try:
        choice = int(input("Enter your choice:"))

        if choice == 1:
            createNewAccount()

        elif choice == 2:
            account = login()
            if account:
                while(1):
                    account_menu()
                    account_choice = int(input("Enter your choice:"))
                    if account_choice == 1:
                        check_balance(account)
                    elif account_choice == 2:
                        deposit(account)
                    elif account_choice == 3:
                        withdraw(account)
                    elif account_choice == 4:
                        show_account_details(account)
                    elif account_choice == 5:
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == 3:
            print("Thank you for using the Bank Management System. Visit again!")
            break

        
    except ValueError:
        print("Invalid choice. Please enter a number.")