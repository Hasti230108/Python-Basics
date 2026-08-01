def welcome():
    print("=== Student Record Manager ===")
    name = input("\nEnter name: ")
    pswd = "teachers@123"
    while(True):
        try:
            password = input("Enter password: ")
            if password == pswd:
                break
            else:
                print("Incorrect password. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
    print(f"\nWelcome {name} to student record manager.")

def menu():
    print("\n1. Add Entry")
    print("2. View Entry")
    print("3. Search Entry")
    print("4. Delete Entry")
    print("5. Exit")