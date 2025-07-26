import tkinter as tk
from tkinter import ttk, messagebox

# --- Main Window ---
root = tk.Tk()
root.title("Tkinter Tutorial with Login")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# --- Panels ---
def open_panel(user_type):
    panel = tk.Toplevel(root)
    panel.title(f"{user_type} Panel")
    panel.geometry("600x500")
    panel.configure(bg="#f0f0f0")

    tk.Label(panel, text=f"Welcome to {user_type} Panel", font=("Arial", 14), bg="#f0f0f0ff").pack(pady=10)

    # --- Form Frame ---
    form_frame = tk.Frame(panel, bg="#fbfafa")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Name", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    tk.Label(form_frame, text="Age", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="e")

    name_entry = tk.Entry(form_frame)
    age_entry = tk.Entry(form_frame)

    name_entry.grid(row=0, column=1, padx=5)
    age_entry.grid(row=1, column=1, padx=5)

    # --- Table Frame ---
    table_frame = tk.Frame(panel)
    table_frame.pack(pady=10, fill="both", expand=True)

    tree = ttk.Treeview(table_frame, columns=("Name", "Age"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)

    # --- Button Actions ---
    def add_record():
        name = name_entry.get().strip()
        age = age_entry.get().strip()

        if not name or not age.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid name and numeric age.")
            return

        tree.insert("", "end", values=(name, age))
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

    def delete_record():
        selected = tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select a record to delete.")
            return
        for item in selected:
            tree.delete(item)

    # --- Buttons ---
    button_frame = tk.Frame(panel, bg="#f0f0f0")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add", command=add_record, bg="#4caf50", fg="white", width=10).pack(side="left", padx=10)
    tk.Button(button_frame, text="edit", command=add_record, bg="#4caf50", fg="white", width=10).pack(side="left", padx=10)
    tk.Button(button_frame, text="Delete", command=delete_record, bg="#cf730a", fg="white", width=10).pack(side="left", padx=10)

# --- Login Functions ---                    
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        open_panel("Admin")
    elif username == "user" and password == "user123":
        open_panel("User")
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")

# --- Login UI ---
login_frame = tk.Frame(root, bg="#f0f0f0")
login_frame.pack(pady=100)

tk.Label(login_frame, text="Username", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

tk.Button(login_frame, text="Login", command=login, bg="#2196f3", fg="white", width=10).pack(pady=10)

# --- Run the App ---
root.mainloop()
