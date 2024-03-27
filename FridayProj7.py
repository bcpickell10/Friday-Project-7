import tkinter as tk
from tkinter import messagebox
import re
import sqlite3

# Create a database connection
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create user table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')
conn.commit()

# Function to validate email format
def validate_email(email):
    return bool(re.match(r'[^@]+@[^@]+\.[^@]+', email))

# Function to validate password confirmation
def validate_password(password, confirm_password):
    return password == confirm_password

# Function to sign up a user
def sign_up():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format!")
        return

    if not validate_password(password, confirm_password):
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Email already exists!")
    else:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully!")
        clear_entries()

# Function to clear entry fields
def clear_entries():
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Create the sign-up window
sign_up_window = tk.Tk()
sign_up_window.title("Sign Up")

email_label = tk.Label(sign_up_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(sign_up_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(sign_up_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(sign_up_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

confirm_password_label = tk.Label(sign_up_window, text="Confirm Password:")
confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
confirm_password_entry = tk.Entry(sign_up_window, show="*")
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

sign_up_button = tk.Button(sign_up_window, text="Sign Up", command=sign_up)
sign_up_button.grid(row=3, column=1, padx=10, pady=5, sticky="e")

# Function to start the application
def start():
    sign_up_window.mainloop()

start()

# Function to sign in a user
def sign_in():
    email = email_entry.get()
    password = password_entry.get()

    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Logged in successfully!")
    else:
        messagebox.showerror("Error", "Email or password incorrect")

# Create the sign-in window
sign_in_window = tk.Tk()
sign_in_window.title("Sign In")

email_label = tk.Label(sign_in_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(sign_in_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(sign_in_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(sign_in_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

sign_in_button = tk.Button(sign_in_window, text="Sign In", command=sign_in)
sign_in_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Function to start the application
def start():
    sign_in_window.mainloop()

start()
