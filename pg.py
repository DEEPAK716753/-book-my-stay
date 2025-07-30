from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
class PG:
    def _init_(self):
        self.root=Tk()
        self.root.title("welcome page")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        self.img=Image.open("imagepg.jpg")
      
        self.img_new=self.img.resize((self.width,self.height))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=0,y=0)
        self.frame1=Frame(self.img_label,bg="#1997f7",width=640,height=654)
        self.frame1.place(x=100,y=56)
       
        self.imgi=Image.open("imagelogo.jpg")
        self.imgi_new=self.imgi.resize((440,240))
        self.imgi_tk=ImageTk.PhotoImage(self.imgi_new)
        self.imgi_label=Label(self.root,image=self.imgi_tk)
        self.imgi_label.place(x=200,y=60)

        # self.welcome=Label(self.frame1,text="Welcome",font=('Georgia',30,"bold"),bg="#1997f7")
        # self.welcome.place(x=220,y=200)
        
        self.btn1=Button(self.frame1,text="Login for Student",font=('Georgia',20,"bold"),bg="#D3E3CD")
        self.btn1.place(x=210,y=300)

        self.btn2=Button(self.frame1,text="Login for Teacher",font=('Georgia',20,"bold"),bg="#D3E3CD")
        self.btn2.place(x=210,y=380)

        self.orr=Label(self.frame1,text="or",font=('Tahoma',18,'bold'),bg='#1997f7')
        self.orr.place(x=330,y=450) 
        
        self.btn3=Button(self.frame1,text="Create Account",font=('Georgia',20,"bold"),bg="#D3E3CD")##1997e7
        self.btn3.place(x=230,y=500)
        
        self.stu=Image.open("pglogo.png")
        self.stunew=self.stu.resize((50,50))
        self.stutk=ImageTk.PhotoImage(self.stunew)

        self.stu_label=Label(self.frame1,image=self.stutk)
        self.stu_label.place(x=147,y=300)

        # self.stu1=Image.open("image1.0.webp")
        # self.stunew1=self.stu1.resize((50,50))
        # self.stutk1=ImageTk.PhotoImage(self.stunew1)

        # self.stu_label1=Label(self.frame1,image=self.stutk1)
        # self.stu_label1.place(x=147,y=380)

        # self.stu2=Image.open("image2.png")
        # self.stunew2=self.stu2.resize((50,50))
        # self.stutk2=ImageTk.PhotoImage(self.stunew2)

        self.stu_label2=Label(self.frame1,image=self.stutk2)
        self.stu_label2.place(x=165,y=500)

        
    
        self.root.mainloop()
obj=PG()