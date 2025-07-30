from tkinter import *
from customtkinter import *
from datetime import datetime
from database import getAllUsers
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import shutil
import os
from tkinter import messagebox
from tkinter import filedialog
import database


class EditPG():
    def __init__(self,window,id):
        self.root= window
        self.id=id
        self.cutom1 = ("Arial", 13, "bold")
        self.data= database.getSinglePg(self.id)
        
        
    
    def clear_main_frame(self):
        # Clear the main frame content before loading new content
        for widget in self.root.winfo_children():
            if widget.winfo_x() == 0:  # Main frame location
                widget.destroy()
    def editSection(self):
        self.clear_main_frame()
        self.main_frame = Frame(self.root, bg='white', width=900, height=500)
        self.main_frame.place(x=0, y=50)

        Label(self.main_frame, text="Add New PG", font=("Arial", 18, "bold"), bg="white").place(x=50, y=20)

        Label(self.main_frame, text="PG Name:", bg="white", font=self.cutom1).place(x=50, y=80)
        self.pg_name = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_name.place(x=200, y=80)
        self.pg_name.insert(0,self.data[1])
        
        Label(self.main_frame, text="Address:", bg="white", font=self.cutom1).place(x=50, y=130)
        self.pg_address = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_address.place(x=200, y=130)
        self.pg_address.insert(0,self.data[2])

        Label(self.main_frame, text="Rent:", bg="white", font=self.cutom1).place(x=50, y=180)
        self.pg_rent = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_rent.place(x=200, y=180)
        self.pg_rent.insert(0,self.data[3])

        Label(self.main_frame, text="Amenities:", bg="white", font=self.cutom1).place(x=50, y=230)
        self.pg_amenities = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_amenities.place(x=200, y=230)
        self.pg_amenities.insert(0,self.data[4])

        Label(self.main_frame, text="Owner Contact:", bg="white", font=self.cutom1).place(x=50, y=280)
        self.pg_owner_id = CTkEntry(self.main_frame, width=240,font=("Arial", 12))
        self.pg_owner_id.place(x=200, y=280)
        self.pg_owner_id.insert(0,self.data[6])
        
        Label(self.main_frame, text="PG Type", bg="white", font=self.cutom1).place(x=50, y=330)
        self.pg_type = CTkComboBox(self.main_frame,values=['Boys','Girls'], width=240, font=("Arial", 12))
        self.pg_type.place(x=200, y=330)
        self.pg_type.set(self.data[5])

        # Upload Picture Button
        CTkButton(master=self.main_frame, text="Upload Picture", fg_color="blue", text_color="white", command=self.upload_file).place(x=200, y=380)

        # Label to display the uploaded image
        self.img_label_display = Label(self.main_frame, bg="white")
        self.img_label_display.place(x=500, y=100, width=150, height=150)

        CTkButton(master=self.main_frame, text="Add PG", fg_color="green", text_color="white", command=self.update_pg_to_db).place(x=350, y=380)
        
    
    def upload_file(self):
        # Open a file dialog and select a file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        
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
                
                # Show the uploaded image in the form
                image = Image.open(self.target_file_path)
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

        
    def update_pg_to_db(self):
        pg_name = self.pg_name.get()
        pg_address = self.pg_address.get()
        pg_rent = self.pg_rent.get()
        pg_amenities = self.pg_amenities.get()
        pg_type = self.pg_type.get()
        pg_owner_id = self.pg_owner_id.get()
        
        # Add database insertion logic here
        print(f"PG Added: {pg_name}, {pg_address}, {pg_rent}, {pg_amenities}, {pg_owner_id}")
        if hasattr(self, 'target_file_path'):
            print(f"Image Path: {self.target_file_path}")
        data= (pg_name,pg_address,pg_rent,pg_amenities,pg_type,pg_owner_id,self.target_file_path,self.id[0])
        res= database.updatePgDetails(data)
        if res:
            messagebox.showinfo("Success", "PG Updated Successfully")
        else:
            messagebox.showerror("Error",'Not Updated')
if __name__=="__main__":
    obj=EditPG()
    obj.editSection()
