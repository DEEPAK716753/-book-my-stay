from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import customtkinter as ctk
import tkinter as tk
from tkinter.ttk import Combobox
# import openpyxl, xlrd
from openpyxl import Workbook
# import pathlib
import shutil
# import dataeduspot
from tkinter import messagebox
from tkinter import filedialog





class register:
    def _init_(self): 
        
        self.root=Tk()
        self.root.title("College Entry form")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        self.img=Image.open("c3.jpg")
        self.img_new=self.img.resize((self.width,self.height))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=0,y=0)
        self.frame1=Frame(self.img_label,bg="lightblue",width=1235,height=654)
        self.frame1.place(x=100,y=56)

        self.head=Label(self.frame1,text="College Details",font=("tohoma",25,"bold"),bg="white",width=62)
        self.head.place(x=0,y=20)

        self.name=Label(self.frame1,text="College Name",font=("arial",15,"normal"),bg="lightblue")
        self.name.place(x=5,y=80)
        self.name_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.name_entry.place(x=5,y=108)
        li=["GNDU","IKGPTU","Chandigarh University","GNA","LPU","Thapar Institute","Chitkara University"]
        self.mon=Label(self.frame1,text="College under Branch",font=("arial",15,"normal"),bg="lightblue")
        self.mon.place(x=5,y=150)
        self.month=ttk.Combobox(self.frame1,values=li)
        self.month.place(x=5,y=178,width=150)
        self.level=Label(self.frame1,text="Rank",font=("arial",15,"normal"),bg="lightblue")
        self.level.place(x=5,y=220)
        self.level_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.level_entry.place(x=5,y=248)
        self.grade=Label(self.frame1,text="Level",font=("arial",15,"normal"),bg="lightblue")
        self.grade.place(x=5,y=290)
        self.grade_entry=ttk.Combobox(self.frame1,value=["tier-1(government)","tier-2(private high status)","tier-3"],width=22)
        self.grade_entry.place(x=5,y=318)
        self.level1=Label(self.frame1,text="College Establishment",font=("arial",15,"normal"),bg="lightblue")
        self.level1.place(x=5,y=360)
        self.level1_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.level1_entry.place(x=5,y=388)
        self.clas=Label(self.frame1,text="Type of College",font=("arial",15,"normal"),bg="lightblue")
        self.clas.place(x=5,y=430)
        li2=["Medical","Engineering","Hotel Management","Art","Business Management","others"]
        self.classes=ttk.Combobox(self.frame1,values=li2)
        self.classes.place(x=5,y=458,width=150)
       
        self.mail=Label(self.frame1,text="Official Email",font=("arial",15),bg="lightblue")
        self.mail.place(x=5,y=500)
        self.mail_entry=Entry(self.frame1,font=("arial",15),bg="#edeff2")
        self.mail_entry.place(x=5,y=528)
        self.phone=Label(self.frame1,text="Phone Number 1",font=("arial",15,"normal"),bg="lightblue")
        self.phone.place(x=5,y=570)
        self.phone_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.phone_entry.place(x=5,y=598)
        self.phonee=Label(self.frame1,text="Phone number 2",font=("arial",15,"normal"),bg="lightblue")
        self.phonee.place(x=300,y=80)
        self.phonee_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.phonee_entry.place(x=300,y=108)
        self.add=Label(self.frame1,text="Address",font=("arial",15,"normal"),bg="lightblue")
        self.add.place(x=300,y=150)
        self.add_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.add_entry.place(x=300,y=178)

        self.staff=Label(self.frame1,text="Staff members",font=("arial",15,"normal"),bg="lightblue")
        self.staff.place(x=300,y=220)
        # self.add_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        # self..place(x=300,y=248)
        li3=[]
        for i in range(10,70):
            li3.append(i)
        self.stafft=ttk.Combobox(self.frame1,values=li3)
        self.stafft.place(x=300,y=248)
        self.p=Label(self.frame1,text="Principal Name",font=("arial",15,"normal"),bg="lightblue")
        self.p.place(x=300,y=290)
        self.p_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.p_entry.place(x=300,y=318)

        self.hp=Label(self.frame1,text="Highest CGPA with degree",font=("arial",15,"normal"),bg="lightblue")
        self.hp.place(x=300,y=360)
        self.hp_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.hp_entry.place(x=300,y=388)
        self.hp1=Label(self.frame1,text="Highest Package",font=("arial",15,"normal"),bg="lightblue")
        self.hp1.place(x=300,y=430)
        self.hp1_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.hp1_entry.place(x=300,y=458)
        
        self.labb=Label(self.frame1,text="Password(Email)",font=("arial",15,"normal"),bg="lightblue")
        self.labb.place(x=300,y=500)
        self.labb_entry=Entry(self.frame1,font=("arial",15,"normal"),show="*",bg="#edeff2")
        self.labb_entry.place(x=300,y=528)
        
        self.tran=Label(self.frame1,text="Transportation Service",font=("arial",15,"normal"),bg="lightblue")
        self.tran.place(x=300,y=570)
        self.tran_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.tran_entry.place(x=300,y=598)

        self.Degree=Label(self.frame1,text="Degree Available",font=("arial",15,"normal"),bg="lightblue")
        self.Degree.place(x=645,y=80)
        var1=IntVar()
        Checkbutton(self.root,text="B-tech",variable=var1).place(x=750,y=170)
        var2=IntVar()
        Checkbutton(self.root,text="BBA",variable=var2).place(x=750,y=200)
        var3=IntVar()
        Checkbutton(self.root,text="B.COM",variable=var3).place(x=750,y=230)
        var4=IntVar()
        Checkbutton(self.root,text="BCA",variable=var4).place(x=820,y=170)
        var5=IntVar()
        Checkbutton(self.root,text="BA",variable=var5).place(x=820,y=200)
        var6=IntVar()
        Checkbutton(self.root,text="MA",variable=var6).place(x=820,y=230)
        var7=IntVar()
        Checkbutton(self.root,text="MBA",variable=var7).place(x=890,y=170)
        var8=IntVar()
        Checkbutton(self.root,text="M-COM",variable=var8).place(x=890,y=200)
        var9=IntVar()
        Checkbutton(self.root,text="Hotel Management",variable=var9).place(x=890,y=230)
        var10=IntVar()
        Checkbutton(self.root,text="BSC",variable=var10).place(x=980,y=170)
        var11=IntVar()
        Checkbutton(self.root,text="MSC",variable=var11).place(x=980,y=200)
        var12=IntVar()
        Checkbutton(self.root,text="others",variable=var12).place(x=1040,y=230)

         
        self.comp1=Label(self.frame1,text="Inhouse Company",font=("arial",15,"normal"),bg="lightblue")
        self.comp1.place(x=645,y=210)
        self.comp1_entry=Entry(self.frame1,font=("arial",15,"normal"),bg="#edeff2")
        self.comp1_entry.place(x=645,y=238)

        
        self.imgi = Image.open("c2.jpg")
        self.imgi_new = self.imgi.resize((300, 250))
        self.imgi_tk = ImageTk.PhotoImage(self.imgi_new)

        self.comp1=Label(self.frame1,text="Add Certificate",font=("arial",15,"normal"),bg="lightblue")
        self.comp1.place(x=730, y=280)
        self.btn = Button(self.frame1, text="Upload Certificate", command=self.upload_file,width=20,bg="#edeff2")
        self.btn.place(x=730, y=600) 
        self.img_label_display = Label(self.frame1, image=self.imgi_tk, bg="white")
        self.img_label_display.place(x=650, y=310) 
        
        self.register=Button(self.frame1,text="Submit",font=("arial",20,"normal"),command=self.getVal)
        self.register.place(x=1060,y=580)

        self.imgii=Image.open("bak.png")
        self.imgii_new=self.imgii.resize((90,50))
        self.imgii_tk=ImageTk.PhotoImage(self.imgii_new)
        self.back_button=tk.Button(self.img_label,text="Back",image=self.imgii_tk,command=self.back,bg="white",border=0)
        self.back_button.place(x=0,y=0)

        
        
        self.root.mainloop()
    def upload_file(self):
        # Open a file dialog and select a file
        file_path = filedialog.askopenfilename()
        
        if file_path:
            try:
                # Define the target directory to save the file
                target_directory = "uploaded_files"
                
                # Create the target directory if it doesn't exist
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                
                # Extract the file name from the file path
                file_name = os.path.basename(file_path)
                
                # Define the target file path
                self.target_file_path = os.path.join(target_directory, file_name)
                
                # Copy the selected file to the target directory
                shutil.copy(file_path, self.target_file_path)
                
                # Show a success message
                image = Image.open(file_path)
                image.thumbnail((150, 150))  # Resize image if necessary
                photo = ImageTk.PhotoImage(image)
                self.img_label_display.config(image=photo)
                self.img_label_display.image = photo  # Keep a reference to avoid garbage collection
                messagebox.showinfo("Success", f"File '{file_name}' uploaded successfully!")
            
            except Exception as e:
                # Show an error message if something goes wrong
                messagebox.showerror("Error", f"Failed to upload file: {str(e)}")
        else:
            messagebox.showwarning("No File", "No file was selected.")

            
    def getVal(self):
        # print("Hi")
        data=(self.name_entry.get(),self.month.get(),self.level_entry.get(),
              self.grade_entry.get(),self.level1_entry.get(),self.classes.get(),self.mail_entry.get(),self.phone_entry.get(),
              self.phonee_entry.get(),self.add_entry.get(),self.stafft.get(),self.p_entry.get(),self.hp_entry.get(),self.hp1_entry.get(),
              self.labb_entry.get(),self.tran_entry.get(),self.comp1_entry.get(),self.target_file_path,"Pending"
               )
        
   #      res= database.getAlluser(data)
   #      print(res)
   #      if res:
   #          messagebox.showinfo("Success","register successfully")
   #          # self.root.destroy()
   #          # teach2.Home()
          
   #      else:
   #          messagebox.showerror("Error","User not exist")
   #  def back(self):
   #      self.root.destroy()
       

r1 = register()


