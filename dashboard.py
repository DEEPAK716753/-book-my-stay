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
import show_pg
import show_en





class dash():
    def __init__(self):
        self.cutom1 = ("Arial", 13, "bold")
        self.root = Tk()
        self.root.title("Dashboard")
        # self.width = self.root.winfo_screenwidth()
        # self.height = self.root.winfo_screenheight()
        self.width = 1300
        self.height = 600
        self.root.geometry(f"{self.width}x{self.height}")

        self.blue_frame = Frame(self.root, bg="#1ac1eb", width=self.width, height=50)
        self.blue_frame.place(x=0, y=0)

        self.sidebar()
        self.coloums()
        self.pie()

        self.logout = CTkButton(master=self.root, text="Logout", fg_color="#1aeb47", text_color="Black", corner_radius=0, hover_color="red", command=self.root.quit)
        self.logout.place(x=1100, y=10)

        # image code
        im = Image.open("9131529.png") 
        img_new = im.resize((100, 100))
        img = ImageTk.PhotoImage(img_new)
        self.label_img = Label(self.root, bg="white", image=img)
        self.label_img.place(x=80, y=80)

        self.root.mainloop()

    def sidebar(self):
        self.frame_side = Frame(self.root, width=300, height=self.height, bg="white")
        self.frame_side.place(x=0, y=0)

        self.name_data = Label(self.frame_side, text="Deepak", bg="white", font=("Arial", 13, "bold"))
        self.name_data.place(x=100, y=200)

        # icons
        self.name_data = Button(self.frame_side, border=0, text="Dashboard", bg="white", font=("Arial", 13, "bold"), command=self.coloums)
        self.name_data.place(x=50, y=300)
        self.name_data = Button(self.frame_side, border=0, text="Enquiry", bg="white", font=("Arial", 13, "bold"), command=self.show_en)
        self.name_data.place(x=50, y=340)
        self.name_data = Button(self.frame_side, border=0, text="Add", bg="white", font=("Arial", 13, "bold"), command=self.show_add_pg_form)
        self.name_data.place(x=50, y=385)
        self.name_data = Button(self.frame_side, border=0, text="Manage", bg="white", font=("Arial", 13, "bold"), command=self.show_pg)
        self.name_data.place(x=50, y=445)
        self.name_data = Button(self.frame_side, border=0, text="Settings", bg="white", font=("Arial", 13, "bold"))
        self.name_data.place(x=50, y=505)
        self.name_data = Button(self.frame_side, border=0, text="Exit", bg="white", font=("Arial", 13, "bold"), command=self.root.quit)
        self.name_data.place(x=50, y=565)
    def coloums(self):
        self.clear_main_frame()
        data = database.allPG()
        total_pgs = len(data)
        total_enquiries = len(database.all_enquiry())
        total_users = len(database.getAllUsers())

        # Create a frame for cards
        card_frame = Frame(self.root, bg="white", width=900, height=500)
        card_frame.place(x=450, y=50)

        # Define card dimensions and padding
        card_width = 200
        card_height = 100
        padding_x = 40
        padding_y = 30
        card_color = "#1ac1eb"

        def create_rounded_card(canvas, x, y, width, height, radius, color):
            points = [
                x + radius, y,
                x + width - radius, y,
                x + width, y, x + width, y + radius,
                x + width, y + height - radius,
                x + width, y + height,
                x + width - radius, y + height,
                x + radius, y + height,
                x, y + height,
                x, y + height - radius,
                x, y + radius,
                x, y
            ]
            return canvas.create_polygon(points, smooth=True, fill=color)

        # Total PGs Card
        canvas_pg = Canvas(card_frame, width=card_width, height=card_height, bg="white", highlightthickness=0)
        canvas_pg.place(x=padding_x, y=padding_y)
        create_rounded_card(canvas_pg, 0, 0, card_width, card_height, 20, card_color)
        canvas_pg.create_text(card_width//2, 30, text="Total PGs", font=("Arial", 14, "bold"), fill="white")
        canvas_pg.create_text(card_width//2, 70, text=str(total_pgs), font=("Arial", 24, "bold"), fill="white")

        # Total Enquiries Card
        canvas_enquiry = Canvas(card_frame, width=card_width, height=card_height, bg="white", highlightthickness=0)
        canvas_enquiry.place(x=padding_x + card_width + padding_x, y=padding_y)
        create_rounded_card(canvas_enquiry, 0, 0, card_width, card_height, 20, card_color)
        canvas_enquiry.create_text(card_width//2, 30, text="Total Enquiries", font=("Arial", 14, "bold"), fill="white")
        canvas_enquiry.create_text(card_width//2, 70, text=str(total_enquiries), font=("Arial", 24, "bold"), fill="white")

        # Total Users Card
        canvas_user = Canvas(card_frame, width=card_width, height=card_height, bg="white", highlightthickness=0)
        canvas_user.place(x=padding_x + 2 * (card_width + padding_x), y=padding_y)
        create_rounded_card(canvas_user, 0, 0, card_width, card_height, 20, card_color)
        canvas_user.create_text(card_width//2, 30, text="Total Users", font=("Arial", 14, "bold"), fill="white")
        canvas_user.create_text(card_width//2, 70, text=str(total_users), font=("Arial", 24, "bold"), fill="white")

    def pie(self):
        res = getAllUsers()
        for i in res:
            print(i)

    def clear_main_frame(self):
        for widget in self.root.winfo_children():
            if widget.winfo_x() == 330:  
                widget.destroy()

    def show_add_pg_form(self):
        self.clear_main_frame()

        self.main_frame = Frame(self.root, bg='white', width=900, height=500)
        self.main_frame.place(x=330, y=50)

        Label(self.main_frame, text="Add New PG", font=("Arial", 18, "bold"), bg="white").place(x=50, y=20)

        Label(self.main_frame, text="PG Name:", bg="white", font=self.cutom1).place(x=50, y=80)
        self.pg_name = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_name.place(x=200, y=80)

        Label(self.main_frame, text="Address:", bg="white", font=self.cutom1).place(x=50, y=130)
        self.pg_address = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_address.place(x=200, y=130)

        Label(self.main_frame, text="Rent:", bg="white", font=self.cutom1).place(x=50, y=180)
        self.pg_rent = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_rent.place(x=200, y=180)

        Label(self.main_frame, text="Amenities:", bg="white", font=self.cutom1).place(x=50, y=230)
        self.pg_amenities = CTkEntry(self.main_frame, width=240, font=("Arial", 12))
        self.pg_amenities.place(x=200, y=230)

        Label(self.main_frame, text="Owner Contact:", bg="white", font=self.cutom1).place(x=50, y=280)
        self.pg_owner_id = CTkEntry(self.main_frame, width=240,font=("Arial", 12))
        self.pg_owner_id.place(x=200, y=280)
        
        Label(self.main_frame, text="PG Type", bg="white", font=self.cutom1).place(x=50, y=330)
        self.pg_type = CTkComboBox(self.main_frame,values=['Boys','Girls'], width=240, font=("Arial", 12))
        self.pg_type.place(x=200, y=330)

        # Upload Picture Button
        CTkButton(master=self.main_frame, text="Upload Picture", fg_color="blue", text_color="white", command=self.upload_file).place(x=200, y=380)

        # Label to display the uploaded image
        self.img_label_display = Label(self.main_frame, bg="white")
        self.img_label_display.place(x=500, y=100, width=150, height=150)

        CTkButton(master=self.main_frame, text="Add PG", fg_color="green", text_color="white", command=self.add_pg_to_db).place(x=400, y=380)

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

    def add_pg_to_db(self):
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
        data= (pg_name,pg_address,pg_rent,pg_amenities,pg_type,pg_owner_id,self.target_file_path)
        res= database.addPgDetails(data)
        if res:
            messagebox.showinfo("Success", "PG Added Successfully")
            message= messagebox.askyesno("Added",'Do you want to add more PG?')
            if message:
                self.main_frame.destroy()
                dash()
            else:
                self.clear_main_frame()
                self.main_frame = Frame(self.root, bg='white', width=900, height=500)
                self.main_frame.place(x=330, y=50)
                show_pg.viewAddPG(self.main_frame)
        else:
            messagebox.showerror("Error",'Not Added')
            
    def show_pg(self):
        self.clear_main_frame()
        self.main_frame = Frame(self.root, bg='white', width=900, height=500)
        self.main_frame.place(x=330, y=50)
        obj= show_pg.viewAddPG(self.main_frame)
        obj.managePG()
             
    def show_en(self):
        self.clear_main_frame()
        self.main_frame = Frame(self.root, bg='white', width=900, height=500)
        self.main_frame.place(x=330, y=50)
        obj= show_en.viewEN(self.main_frame)
        obj.manageEN()
        
if __name__=='__main__':
    d1 = dash()
