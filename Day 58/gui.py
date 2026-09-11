import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq
import pandas as pd

def submit_data():
    username = username_entry.get()
    password = password_entry.get()

    user_data = {
        "username": username,
        "password": password
    }

    connection = sq.connect("Users.db")
    cursor = connection.cursor()

    cursor.execute(
        "insert into users(username, password) values (?, ?)",
        (user_data["username"], user_data["password"])
    )

    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "User data submitted successfully!")

def verify_data():
    username = username_entry.get()
    password = password_entry.get()

    login_data = {
        "username": username,
        "password": password
    }

    connection = sq.connect("Users.db")

    df = pd.read_sql_query("select * from users", connection)

    connection.close()

    result = df[
        (df["username"] == login_data["username"]) &
        (df["password"] == login_data["password"])
    ]

    if not result.empty:
        messagebox.showinfo("Verified", "User credentials are correct!")
    else:
        messagebox.showerror("Failed", "Invalid username or password!")

root = tk.Tk()
root.title("User Login System")
root.geometry("400x250")

tk.Label(root, text="User ID").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Submit", command=submit_data).pack(pady=10)
tk.Button(root, text="Verify", command=verify_data).pack()

root.mainloop()