# Day 12 - File Handling

## Topics Covered

- File Handling
- Creating Files
- Writing to Files
- Reading Files
- Appending Data
- File Reading Methods
- File Pointer
- seek()
- with open()
- Copying Files
- Mini File-Based Project

## Programs

### 1. create_file.py
- Create a new text file (`college.txt`).
- Store user details like name, college, and course.

### 2. write_file.py
- Write student details into `student.txt`.
- Practice writing user input to a file.

### 3. read_file.py
- Read and display the complete contents of a file.

### 4. append_file.py
- Append additional information to an existing file without removing previous data.

### 5. read_methods.py
- Demonstrate the difference between:
  - `read()`
  - `readline()`
  - `readlines()`
- Learn how the file pointer works.
- Use `seek()` to move the file pointer back to the beginning.

### 6. with_open.py
- Use the `with open()` statement.
- Automatically close files after completing operations.

### 7. copy_file.py
- Read the contents of one file.
- Copy the data into another file (`backup.txt`).

### 8. student_record.py
- Create a simple Student Record System.
- Accept student details from the user.
- Store records in `student_record.txt`.
- Read and display all stored records.

## Concepts Learned

- File Modes:
  - `r` (Read)
  - `w` (Write)
  - `a` (Append)
- Reading complete files.
- Reading one line at a time.
- Reading all lines as a list.
- Understanding the file pointer.
- Using `seek()` to reposition the file pointer.
- Automatic file handling with `with open()`.
- Copying data between files.
- Building a simple file-based record system.

## Outcome

Today I learned how to work with files in Python by creating, reading, writing, and appending data. I explored different file reading methods, understood how the file pointer moves, used `seek()` to reposition it, and learned why `with open()` is the recommended approach for file handling. Finally, I combined these concepts to build a simple Student Record System that stores and retrieves data from a text file.