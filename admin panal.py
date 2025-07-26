import tkinter as tk
from tkinter import messagebox

# Sample login credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def verify_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        open_admin_panel()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

def open_admin_panel():
    login_window.destroy()
    admin_window = tk.Tk()
    admin_window.title("Admin Panel")
    admin_window.geometry("1024x720")

    tk.Label(admin_window, text="Welcome to the Admin Panel!", font=("Arial", 16)).pack(pady=20)

    tk.Button(admin_window, text="Manage Users", command=lambda: print("User management")).pack(pady=5)
    tk.Button(admin_window, text="Settings", command=lambda: print("Settings section")).pack(pady=5)
    tk.Button(admin_window, text="View Reports", command=lambda: print("Reports section")).pack(pady=5)

    admin_window.mainloop()

# Login Window
login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("1024x720")

tk.Label(login_window, text="Username").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=verify_login).pack(pady=20)

login_window.mainloop()