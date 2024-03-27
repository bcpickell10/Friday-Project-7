import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create user table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')
conn.commit()

# Function to sign up a user
def sign_up():
    email = email_entry.get()
    password = password_entry.get()

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Email already exists!")
    else:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully!")

# Function to sign in a user
def sign_in():
    email = email_entry.get()
    password = password_entry.get()

    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Logged in successfully!")
    else:
        messagebox.showerror("Error", "Invalid email or password")

# Create the sign-up window
sign_up_window = tk.Tk()
sign_up_window.title("Sign Up")

email_label = tk.Label(sign_up_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(sign_up_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(sign_up_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(sign_up_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

sign_up_button = tk.Button(sign_up_window, text="Sign Up", command=sign_up)
sign_up_button.grid(row=2, column=1, padx=10, pady=5)

# Create the sign-in window
sign_in_window = tk.Tk()
sign_in_window.title("Sign In")

email_label = tk.Label(sign_in_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(sign_in_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(sign_in_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(sign_in_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

sign_in_button = tk.Button(sign_in_window, text="Sign In", command=sign_in)
sign_in_button.grid(row=2, column=1, padx=10, pady=5)

sign_up_window.mainloop()
sign_in_window.mainloop()

# Close the database connection when application exits
conn.close()
