import tkinter as tk
from tkinter import messagebox
import db
import csv
import os
# Create the main window
root = tk.Tk()
root.title("User Registration")
root.geometry("1024x720")

# Function to save user info
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    if not username or not password or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email address!")
        return

    # Save to CSV
    file_exists = os.path.isfile("users.csv")
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Password", "Email"])
        writer.writerow([username, password, email])

    messagebox.showinfo("Success", "User registered successfully!")

    # Clear the fields
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# GUI Labels and Entries
tk.Label(root, text="User Registration", font=("Arial", 18)).pack(pady=20)

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root, width=30)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=30)
entry_email.pack()

tk.Label(root, text="City").pack()
entry_password = tk.Entry(root, width=30, show="")
entry_password.pack()

tk.Label(root, text="Address").pack()
entry_password = tk.Entry(root, width=30, show="")
entry_password.pack()

tk.Label(root, text="Phone number").pack()
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

tk.Button(root, text="Register", command=register_user).pack(pady=20)

# Start the main loop
root.mainloop()