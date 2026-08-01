# Day 17 - Student Record Manager (Python)

## Topics Covered

- File Handling
- Functions
- Modules
- Reading Files
- Writing Files
- Searching Records
- Deleting Records
- User Menu
- Basic Authentication

## Project Structure

```
Day 17/
│
├── main.py
├── student.py
├── utils.py
├── students.txt
└── README.md
```

## Project Description

This project is a simple **Student Record Manager** built using Python modules and file handling. It allows users to store and manage student records through a menu-driven interface.

The project is divided into multiple modules to improve readability, maintainability, and code organization.

## Features

- Add Student Record
- View All Student Records
- Search Student by Roll Number
- Delete Student Record
- Password Protected Access
- Modular Code Structure

## Modules

### `main.py`
Controls the entire application, displays the menu repeatedly, and calls the required functions based on the user's choice.

### `student.py`
Contains all functions related to student record management:
- Add Record
- Display Records
- Search Record
- Delete Record

### `utils.py`
Contains helper functions:
- Welcome Screen
- Password Verification
- Menu Display

## File Used

```
students.txt
```

All student records are stored in the following format:

```
Name, Roll Number, Course
```

## Concepts Learned

- Organizing projects using multiple Python modules
- Creating reusable functions
- Reading and writing text files
- Searching data inside files
- Deleting records from files
- Using loops for menu-driven applications
- Applying basic password authentication
- Separating program logic from utility functions

## Outcome

By completing this project, I learned how to organize Python code into multiple modules and build a real-world menu-driven application using file handling. I practiced storing, retrieving, searching, and deleting data from text files while improving my understanding of functions, loops, and modular programming. This project strengthened my confidence in writing structured Python programs and prepared me for building larger applications in the future.