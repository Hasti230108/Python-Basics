from student import add_record, display_records, search_records, delete_record
from utils import welcome, menu

welcome()

while True:
    menu()
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if choice == 1:
        add_record()

    elif choice == 2:
        display_records()

    elif choice == 3:
        search_records()

    elif choice == 4:
        delete_record()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")