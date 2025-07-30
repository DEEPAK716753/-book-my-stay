import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import database
import gmap
import time


class PGManagementSystem:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("PG Listings")
        self.root.geometry("930x500")

        # ctk.set_appearance_mode("light")

        # Initialize UI Components
        self.setup_main_frame()
        self.setup_filter_frame()
        self.setup_scrollable_frame()
        self.load_pg_listings()
        self.root.mainloop()
    def setup_main_frame(self):
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        title = tk.Label(self.main_frame, text="Available PGs", font=("Helvetica", 24, "bold"))
        title.pack(pady=10)

    def setup_filter_frame(self):
        filter_frame = ctk.CTkFrame(self.main_frame)
        filter_frame.pack(pady=10)

        tk.Label(filter_frame, text="Filter by Location:", font=("Helvetica", 14)).pack(side="left", padx=5)
        
        self.location_var = tk.StringVar()
        self.location_combobox = ttk.Combobox(filter_frame, textvariable=self.location_var, font=("Helvetica", 14))
        self.location_combobox['values'] = self.get_all_locations()  # Fetch all unique locations from the database
        self.location_combobox.pack(side="left", padx=5)

        tk.Label(filter_frame, text="Min Price:", font=("Helvetica", 14)).pack(side="left", padx=5)
        self.min_price_var = tk.StringVar()
        self.min_price_entry = ctk.CTkEntry(filter_frame, textvariable=self.min_price_var, font=("Helvetica", 14))
        self.min_price_entry.pack(side="left", padx=5)

        tk.Label(filter_frame, text="Max Price:", font=("Helvetica", 14)).pack(side="left", padx=5)
        self.max_price_var = tk.StringVar()
        self.max_price_entry = ctk.CTkEntry(filter_frame, textvariable=self.max_price_var, font=("Helvetica", 14))
        self.max_price_entry.pack(side="left", padx=5)

        filter_button = ctk.CTkButton(filter_frame, text="Filter", command=self.filter_pgs)
        filter_button.pack(side="left", padx=5)

        clear_button = ctk.CTkButton(filter_frame, text="Clear", command=self.clear_filter)
        clear_button.pack(side="left", padx=5)

    def get_all_locations(self):
        locations = database.allPG()
        address = [i[2] for i in locations]
        address = set(address)
        address = list(address)
        return address

    def setup_scrollable_frame(self):
        self.canvas = tk.Canvas(self.main_frame)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, width=930)
        
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")

    def fetch_pg_details(self, location=None, min_price=None, max_price=None):
        self.pg_list = database.get_pgs_by_filters(location, min_price, max_price)
        return self.pg_list

    def create_pg_card(self, pg):
        id, name, location, price, amenities, p_type, cont, image_path = pg

        img = Image.open(image_path)
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)

        card_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=15, width=700, height=200)
        card_frame.pack(pady=10, padx=(147, 147))

        img_label = tk.Label(card_frame, image=photo)
        img_label.image = photo
        img_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        tk.Label(card_frame, text=name, font=("Helvetica", 16, "bold")).grid(row=0, column=1, sticky="w")
        tk.Label(card_frame, text=f"Location: {location}", font=("Helvetica", 14)).grid(row=1, column=1, sticky="w")
        tk.Label(card_frame, text=f"Rent: Rs.{price}/month", font=("Helvetica", 14)).grid(row=1, column=2, sticky="w")
        tk.Label(card_frame, text=f"Amenities: {amenities}", font=("Helvetica", 14), wraplength=200).grid(row=2, column=1, columnspan=2, sticky="w")

        view_button = ctk.CTkButton(card_frame, text="View Details", command=lambda: self.view_pg_details(pg))
        view_button.grid(row=3, column=0, columnspan=2, pady=10)

    def view_pg_details(self, pg):
        id, name, location, price, amenities, p_type, cont, image_path = pg
        
        self.detail_window = ctk.CTkToplevel(self.root)
        self.detail_window.title("PG Details")
        self.detail_window.geometry("400x600")
        
        self.detail_window.lift()
        self.detail_window.focus_set()
        
        self.img = Image.open(image_path)
        self.img =self.img.resize((300, 200))
        self.photo = ImageTk.PhotoImage(self.img)
        
        self.img_label = tk.Label(self.detail_window, image=self.photo)
        self.img_label.image = self.photo
        self.img_label.pack(pady=10)
        
        tk.Label(self.detail_window, text=name, font=("Helvetica", 18, "bold")).pack(pady=5)
        tk.Label(self.detail_window, text=f"Location: {location}", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self.detail_window, text=f"Rent: Rs.{price}/month", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self.detail_window, text=f"Type: {p_type}", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self.detail_window, text=f"Contact: {cont}", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self.detail_window, text=f"Amenities: {amenities}", font=("Helvetica", 14), wraplength=300).pack(pady=10)
        
        view_button = ctk.CTkButton(self.detail_window, text="View On Map", command=lambda: self.view_on_map(pg)).pack(pady=10)
        
     

        enquire_button = ctk.CTkButton(self.detail_window, text="Enquire", command=lambda: self.open_enquiry_form(pg)).pack(pady=10)
        
        self.detail_window.grab_set()

    def open_enquiry_form(self, pg):
        id, name, location, price, amenities, p_type, cont, image_path = pg
        self.detail_window.destroy()
        enquiry_window = ctk.CTkToplevel(self.root)
        enquiry_window.title("PG Enquiry")
        enquiry_window.geometry("400x600")

        tk.Label(enquiry_window, text="PG Enquiry Form", font=("Helvetica", 18, "bold")).pack(pady=10)

        tk.Label(enquiry_window, text="PG ID:", font=("Helvetica", 14)).pack(pady=5)
        pg_id_label = tk.Label(enquiry_window, text=id, font=("Helvetica", 14))
        pg_id_label.pack(pady=5)

        tk.Label(enquiry_window, text="Your Name:", font=("Helvetica", 14)).pack(pady=5)
        self.user_name_var = tk.StringVar()
        name_entry = ctk.CTkEntry(enquiry_window, textvariable=self.user_name_var, font=("Helvetica", 14))
        name_entry.pack(pady=5)

        tk.Label(enquiry_window, text="Your Email:", font=("Helvetica", 14)).pack(pady=5)
        self.user_email_var = tk.StringVar()
        email_entry = ctk.CTkEntry(enquiry_window, textvariable=self.user_email_var, font=("Helvetica", 14))
        email_entry.pack(pady=5)

        tk.Label(enquiry_window, text="Enquiry Message:", font=("Helvetica", 14)).pack(pady=5)
        self.enquiry_message_var = tk.StringVar()
        enquiry_message_entry = ctk.CTkEntry(enquiry_window, textvariable=self.enquiry_message_var, font=("Helvetica", 14), width=300, height=100)
        enquiry_message_entry.pack(pady=5)
        
        submit_button = ctk.CTkButton(enquiry_window, text="Submit Enquiry", command=lambda: self.submit_enquiry(id))
        submit_button.pack(pady=20)

    def submit_enquiry(self, pg_id):
        user_name = self.user_name_var.get()
        user_email = self.user_email_var.get()
        enquiry_message = self.enquiry_message_var.get()

        print(f"Enquiry Submitted!\nPG ID: {pg_id}\nName: {user_name}\nEmail: {user_email}")
        enquire_data= (pg_id,user_name,user_email,enquiry_message)
        res= database.add_enquiry(enquire_data)
        if res:
            messagebox.showinfo("Saved","Owner will contact you soon!")
        else:
            messagebox.showerror("Error","Not Saved")
        
    def view_on_map(self,pg):
        self.detail_window.destroy()
        time.sleep(2)
        gmap.Map(pg[2])
        
        
    def load_pg_listings(self, location=None, min_price=None, max_price=None):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        pgs = self.fetch_pg_details(location, min_price, max_price)
        print("--Here are Details of PG---",pgs)
        for pg in pgs:
            self.create_pg_card(pg)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def filter_pgs(self):
        selected_location = self.location_var.get()
        min_price = self.min_price_var.get() or None
        max_price = self.max_price_var.get() or None

        if selected_location or min_price or max_price:
            self.load_pg_listings(location=selected_location, min_price=min_price, max_price=max_price)
        else:
            self.load_pg_listings()

    def clear_filter(self):
        self.location_combobox.set('')
        self.min_price_var.set('')
        self.max_price_var.set('')
        self.load_pg_listings()

if __name__ == "__main__":
    # root = ctk.CTk()
    app = PGManagementSystem()
    
