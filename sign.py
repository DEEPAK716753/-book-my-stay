from customtkinter import *
from tkinter import *
import database
#import re
from tkinter import messagebox
from PIL import ImageTk, Image
import tree

class Login1():
    def __init__(self):
        self.root = Tk()
        self.root.title("Sign-Up")
        self.root.geometry("930x500")
        self.root.resizable(False, False)

        self.root.configure(bg="white")

        # image code 
        im = Image.open("sign.png") 
        img_new= im.resize((400,400))
        img = ImageTk.PhotoImage(img_new)
        self.label = Label(self.root , bg="white" , image = img)
        self.label.place(x=50 , y=50)

        # welcome tage code
        self.Label1 = Label(self.root , text = "Welcome Back !!", bg='white' ,  font= ("consolas" , 20 , 'bold'))
        self.Label1.place(x=540 , y=26)

        # input codes 
        # Name entry
        self.user_name = Label(self.root, text= "Your  Name", bg="white" , font= ("Serif" , 9 ))
        self.user_name.place(x=520 , y= 130)
        self.user_entry = Entry(self.root , border=2,   font= ("Serif" , 15 ))
        self.user_entry.place(x= 520 , y= 160)
      
      
        # password entry
        self.user_pass = Label(self.root, text= "Password" ,bg="white" , font= ("Serif" , 9 ))
        self.user_pass.place(x=520 , y= 200)
        self.user_pass_entry = Entry(self.root , border=2, text = "password" , font= ("Serif" , 15 ) , show= "*")
        self.user_pass_entry.place(x= 520 , y= 230)

       
        
        # button 
        self.button1 = CTkButton(master = self.root ,  text = "Login" , bg_color = "blue" , corner_radius= 9 , command=self.getval)
        self.button1.place(x= 520 , y= 290)

        # login 
        self.label_login = Label(self.root, text= "Don't have an account ?" ,bg="white" , font= ("Serif" , 9 ) )
        self.label_login.place(x= 500 , y= 350)
        
        self.root.mainloop()

    def getval(self):
        self.password = self.user_pass_entry.get()
        self.naam = self.user_entry.get()

        data = (self.naam , self.password )

        getdata = database.getAllUsers()

        for i in getdata:
            print(i)
            if self.naam and self.password in i :
                print(data)
                self.root.destroy()
                obj = tree.All()
                return
            else:
                messagebox.showerror("Error" , "No User Name Found")
                return
            
l1 = Login1()
    
                

        

