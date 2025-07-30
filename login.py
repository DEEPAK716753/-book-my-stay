from tkinter import *
# import database
from tkinter import messagebox
from PIL import ImageTk, Image
import register
import login 
import database
import customtkinter as ctk
import allpgs_user

class Login():
    def __init__(self):
        self.root = Tk()
        self.root.title("Sign-Up")
        self.root.geometry("930x500")
        self.root.resizable(False, False)
      
        self.root.configure(bg="white")
        # image code 
        self.im = Image.open("imagepg.jpg") 
        self.img_new= self.im.resize((400,400))
        self.img = ImageTk.PhotoImage(self.img_new)
        self.label = Label(self.root , bg="white" , image =self.img)
        self.label.place(x=50 , y=50)

        # welcome tage code
        self.Label1 = Label(self.root , text = "Welcome Back !!", bg='white' ,  font= ("consolas" , 20 , 'bold'))
        self.Label1.place(x=540 , y=26)

        # input codes 
        # Name entry
        self.user_name = Label(self.root, text= "Email", bg="white" , font= ("Serif" , 11 ))
        self.user_name.place(x=520 , y= 130)
        self.user_entry = Entry(self.root , border=2,   font= ("Serif" , 10 ))
        self.user_entry.place(x= 520 , y= 160)
      
      
        # password entry
        self.user_pass = Label(self.root, text= "Password" ,bg="white" , font= ("Serif" , 11 ))
        self.user_pass.place(x=520 , y= 200)
        self.user_pass_entry = Entry(self.root , border=2, text = "password" , font= ("Serif" , 10 ) , show= "*")
        self.user_pass_entry.place(x= 520 , y= 230)

       
        
        # button 
        self.button1 = Button(master = self.root ,  text = "Login", command=self.user_login )
        self.button1.place(x= 520 , y= 290)

        # login 
        self.label_login = Label(self.root, text= "Don't have an account ?" ,bg="white" , font= ("Serif" , 11 ) )
        self.label_login.place(x= 500 , y= 350)
        
        self.register_button = Button(self.root, text="Register", bd=0, bg="white", fg="blue", cursor="hand2", font=("Serif", 9), command=self.register)
        self.register_button.place(x=670, y=350)

        self.root.mainloop()
        
    def register(self):
        self.root.destroy()
        register.Register()
        
    def user_login(self):
        data= (self.user_entry.get(), self.user_pass_entry.get())
        res= database.login(data)
        
        if res:
            messagebox.showinfo("Success", "Login Successfully")
            self.root.destroy()
            allpgs_user.PGManagementSystem()
            
        else:
            messagebox.showerror("Error","User Not Exist")
            
            

if __name__=="__main__":
       obj=Login()