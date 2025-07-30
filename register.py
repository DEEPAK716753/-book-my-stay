from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import database
import login


class Register():
    def __init__(self):
        self.root = Tk()
        self.root.title("User Registration")
        self.root.geometry("930x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        # Image code
        self.im = Image.open("imagepg.jpg") 
        self.img_new = self.im.resize((400, 400))
        self.img = ImageTk.PhotoImage(self.img_new)
        self.label = Label(self.root, bg="white", image=self.img)
        self.label.place(x=50, y=50)

        # Welcome text
        self.Label1 = Label(self.root, text="Create an Account", bg='white', font=("consolas", 20, 'bold'))
        self.Label1.place(x=540, y=26)

        # Username entry
        self.user_name = Label(self.root, text="Your Name", bg="white", font=("Serif" , 11 ))
        self.user_name.place(x=520, y=100)
        self.user_entry = Entry(self.root, border=2, font=("Serif" , 10 ))
        self.user_entry.place(x=520, y=130)

        # Email entry
        self.user_email = Label(self.root, text="Email Address", bg="white", font=("Serif" , 11 ))
        self.user_email.place(x=520, y=170)
        self.user_email_entry = Entry(self.root, border=2, font=("Serif" , 10 ))
        self.user_email_entry.place(x=520, y=200)

        # Password entry
        self.user_pass = Label(self.root, text="Password", bg="white", font=("Serif" , 11 ))
        self.user_pass.place(x=520, y=240)
        self.user_pass_entry = Entry(self.root, border=2, font=("Serif" , 10 ), show="*")
        self.user_pass_entry.place(x=520, y=270)

        # Contact entry
        self.user_contact = Label(self.root, text="Contact Number", bg="white", font=("Serif" , 11 ))
        self.user_contact.place(x=520, y=310)
        self.user_contact_entry = Entry(self.root, border=2, font=("Serif" , 10 ))
        self.user_contact_entry.place(x=520, y=340)

        # Register button
        self.button1 = Button(master=self.root, text="Register", command=self.register_user)
        self.button1.place(x=520, y=390)

        self.root.mainloop()

    def register_user(self):
        name = self.user_entry.get()
        email = self.user_email_entry.get()
        password = self.user_pass_entry.get()
        contact = self.user_contact_entry.get()
        
        if not name or not email or not password or not contact:
            messagebox.showerror("Error", "All fields are required!")
        else:
            data= (name,email,password,contact)
            res = database.register(data)
            if res:
                messagebox.showinfo("Success", "Registration Successful!")
                self.root.destroy()
                login.Login()
            else:
                messagebox.showerror("Error","Not Registered")
                
            


if __name__=='__main__':
    Register()