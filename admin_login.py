from customtkinter import *
from PIL import Image
import database
import dashboard
from tkinter import messagebox

class AdminLoginPage:
    def __init__(self):
        self.main = CTk()
        self.main.title("Admin Login Page")
        self.main.config(bg="white")
        self.main.resizable(False, False)

        self.bg_img = CTkImage(dark_image=Image.open("9131529.png"), size=(500, 500))

        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.grid(row=0, column=0)

        self.frame1 = CTkFrame(self.main, fg_color="#D9D9D9", bg_color="white", height=350, width=300, corner_radius=20)
        self.frame1.grid(row=0, column=1, padx=40)

        self.title = CTkLabel(self.frame1, text="Admin Login\nAccess Your Dashboard", text_color="black", font=("", 35, "bold"))
        self.title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

        self.usrname_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                                      font=("", 16, "bold"), width=200, corner_radius=15, height=45)
        self.usrname_entry.grid(row=1, column=0, sticky="nwe", padx=30)

        self.passwd_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Password", fg_color="black", placeholder_text_color="white",
                                      font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
        self.passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)

        self.l_btn = CTkButton(self.frame1, text="Login", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF", cursor="hand2", corner_radius=15, command=self.login_user)
        self.l_btn.grid(row=3, column=0, sticky="nsew", pady=20, padx=35)

        self.main.mainloop()

    def login_user(self):
        data = (self.usrname_entry.get(), self.passwd_entry.get())
        res = database.adminLogin(data)  # Assuming you have a loginAdmin function
        if res:
            messagebox.showinfo("Success", "Login Successfully")
            self.main.destroy()
            dashboard.dash()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

if __name__ == '__main__':
    obj = AdminLoginPage()
