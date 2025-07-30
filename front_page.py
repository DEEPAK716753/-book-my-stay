from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class front_page():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("PG Nest")
        self.displ_width = self.root.winfo_screenwidth()
        self.displ_height = self.root.winfo_screenheight()
        self.root.configure(bg="white")
        self.root.geometry(f"{self.displ_width}x{self.displ_height}")
        # self.root.resizable(False,False)

        self.navbar()
        self.main_heading()
        self.root.mainloop()
        
    def navbar(self):
        self.theme = "red"
        self.cutom = ("Montserrat" , 20 , "bold")
        self.cutom1 = ("Arial" , 13, "bold")
        self.cutom2 = ("Arial" , 12, "bold")
        
        self.frame_red = Frame(self.root , bg= self.theme , width=self.displ_width, height=45)
        self.frame_red.place(x=0 , y=0)
        
        
        self.main_name = CTkLabel(master= self.root , text="PG Nest" , bg_color=self.theme , text_color="white" , text_font=self.cutom)
        self.main_name.place(x= 20 , y = 10)

        self.main_state_name = CTkLabel(master= self.root , text="Jalandhar" , bg_color=self.theme , text_color="white" , text_font=self.cutom1 )
        self.main_state_name.place(x= 160 , y = 10)

        login_header = CTkLabel(master= self.root , text="Login" , bg_color="red" , text_color="white" , border = 0 , text_font=self.cutom1)
        login_header.place(x= 1020 , y = 10)

        post = CTkButton(master= self.root , text="Post Room" , fg_color="red" , text_color="white" , corner_radius= 0 ,text_font=self.cutom2 , hover_color="red")
        post.place(x= 1130 , y = 8)

    def main_heading(self):
        self.main_label = CTkLabel(master= self.root , text= "Welcome to PG Nest !!" , text_font=self.cutom )
        self.main_label.place(x = 100, y= 65)
        



obj1 = front_page()
    
    
