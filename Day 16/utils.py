def welcome():
    print("==== PYTHON ATM ====")

    name = input("\nAccount Holder Name: ")
    while(1):
        try:
            AccNo = int(input("Account No.: "))
            break 
        except ValueError:
            print("Wriong Acc Number.")
         
    print(f"\nWelcome {name}!")

    return name, AccNo

def menu():
    print("\n==== MENU ====")
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

