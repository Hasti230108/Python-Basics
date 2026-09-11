# Day 58 — User Login GUI Mini Project

## Project Overview

A simple User Login System built using Python.

The project provides a GUI where users can submit their User ID and Password and verify whether the credentials already exist in the database.

## Library and Tech Used

- Python
- Tkinter
- SQLite
- Pandas
- Dictionaries

## Features

- User-friendly GUI
- User ID and Password input
- Submit user data to SQLite database
- Verify stored credentials
- Pandas used to read and check database data
- Two dictionaries used for Submit and Verify operations
- Password field is hidden in the GUI

## Project Structure

### database.py
Creates the SQLite database and `users` table.

### gui.py

Contains the Tkinter GUI, Submit functionality and Verify functionality.

### main.py

Acts as the entry point of the project and starts the GUI.

### .gitignore

Prevents database files and Python cache files from being uploaded to GitHub.

## How to Run

Run the project using:

```bash
python main.py
```

## Testing

The project was tested with:

* Correct credentials → Verification successful
* Incorrect credentials → Verification failed
* Submitted credentials → Successfully stored in SQLite database

## Learning Outcomes

* Created a GUI using Tkinter
* Connected Python with SQLite
* Used Pandas with SQLite data
* Used dictionaries as key-value pairs
* Practiced modular Python programming
* Learned to use `.gitignore`
* Built a complete mini project