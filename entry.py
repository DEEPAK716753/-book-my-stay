from tkinter import *
from customtkinter import *
from PIL import Image , ImageTk
import login


class Entry():
    def __init__(self):
        self.root = Tk()
        self.root.title("PG Nest")
        self.root.geometry("900x500")
        self.root.resizable(False,False)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        im = Image.open("entry.jpeg") 
        img_new= im.resize((500,480))
        img = ImageTk.PhotoImage(img_new)
        self.label = Label(self.root , bg="white", border=0 , image = img)
        self.label.place(x=0 , y=0)

        #logo 
        im1 = Image.open("logo.jpg") 
        img_new1= im1.resize((200,100))
        img1 = ImageTk.PhotoImage(img_new1)
        self.label_img = Label(self.root , bg="white" ,border=0, image = img1)
        self.label_img.place(x=0 , y=0)

        self.entries()
        self.root.mainloop()

    def entries(self):
        self.heading = Label(self.root , text="Welcome to PG Nest !!" , font= ("Arial",20,"bold"))
        self.heading.place(x=540 , y= 30)
        self.buttons()

        self.footer = Label(self.root , text="Contact = PG_Nest@gmail.com")
        self.footer.place(x=720 , y= 480)        
     

        
    def buttons(self):
        self.heading = Label(self.root , text="Already Have account ??" , font= ("Arial",10))
        self.heading.place(x=540 , y= 110)
        self.heading_button = CTkButton(master =self.root , text="Sign-In" , bg="#f1f1f1" ,  width=100,command=self.signIn)
        self.heading_button.place(x=540 , y=140)

        # login button
        self.heading = Label(self.root , text="Donot have Account ??" , font= ("Arial",10))
        self.heading.place(x=540 , y= 200)
        self.heading_button = CTkButton(master =self.root , text="Log-In" , bg="#f1f1f1" ,  width=100, command=self.openLogin)
        self.heading_button.place(x=540 , y=230)

        # User Account
        self.heading = Label(self.root , text="Are you a PG Owner ?" , font= ("Arial",10))
        self.heading.place(x=540 , y= 290)
        self.heading_button = CTkButton(master =self.root , text="Log-In"  ,  width=100, command=self.openUser)
        self.heading_button.place(x=540 , y=320)

    def openLogin(self):
        self.root.destroy()
        login.Login()
        
    def openUser(self):
        self.root.destroy()
    def signIn(self):
        self.root.destroy()
        
        

e1 = Entry()

