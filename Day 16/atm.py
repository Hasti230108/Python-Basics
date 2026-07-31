def check_balance(balance):
    print(f"Current Balance: {balance}")

def deposit(balance, amount):

    if amount <= 0:
        print("Invalid amount.")
        return balance

    balance += amount

    print("Amount Deposited SUccessfully.")
    print(f"Updated Balance: {balance}")

    return balance

def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
        return balance

    if amount > balance:
        print("Insufficient balance.")
        return balance

    balance -= amount

    print("Amount withdrawn successfully.")
    print(f"Updated Balance: {balance}")

    return balance