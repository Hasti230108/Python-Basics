# Day 18 - Bank Management System (Python)

## Topics Covered
- Python Modules
- File Handling
- Functions
- Exception Handling
- Loops
- Conditional Statements
- Random Module
- User Input Validation

## Project Structure

```
Day 18/
│
├── main.py
├── bank.py
├── utils.py
├── accounts.txt
└── README.md
```

---

## Features

### Create New Account
- Creates a new bank account.
- Generates a unique account number.
- Stores account details in a text file.

### Login
- Login using the account number.

### Check Balance
- Displays the current account balance.

### Deposit Money
- Adds money to the account.
- Updates the balance in the file.

### Withdraw Money
- Withdraws money if sufficient balance is available.
- Prevents withdrawing more than the available balance.

### Show Account Details
Displays:
- Account Number
- Name
- Age
- Phone Number
- Email Address
- Balance

### Logout
Returns to the main menu.

## Validations

- Age must be **18 or above**
- Phone number must contain **exactly 10 digits**
- Email must contain **@** and **.**
- Deposit amount must be a valid number
- Withdrawal amount cannot exceed available balance
- Automatically generates a **unique account number**

## Data Storage

All account information is stored inside:

```
accounts.txt
```

Each record is saved in the following format:

```
Account Number: ACC123456, Name: Hasti, Age: 18, Phone: 9876543210, Email: hasti@gmail.com, Balance: 5000.0
```

## Technologies Used

- Python
- File Handling
- Random Module

## Concepts Learned

- Modular Programming
- Reading and Writing Files
- Updating File Records
- Exception Handling
- Data Validation
- Functions
- Loops
- Python Modules
- String Manipulation

## Outcome

By completing this project, I learned how to build a modular Python application that simulates a basic banking system. I implemented features such as account creation, secure login using account numbers, balance inquiry, deposits, withdrawals, and account detail management using file handling. I also added input validation for age, phone number, email, and transaction amounts, along with automatic generation of unique account numbers. This project strengthened my understanding of Python modules, file operations, exception handling, functions, loops, and real-world program organization while improving my problem-solving and debugging skills.