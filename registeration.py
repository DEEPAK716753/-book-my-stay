from tkinter import *
from customtkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox


class PG():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("PG Registeration")
        self.width = self.root.winfo_screenwidth() 
        self.height = self.root.winfo_screenheight() 
        self.root.geometry(f"{self.width}x{self.height}")
        # self.root.resizable(False, False)
        self.root.configure(bg="lightblue")
        self.font = ("Arial" , 15)
        self.lightgrey_color = "#edeff2"
        self.color_lightblue = "lightblue"
        self.PG_entries()
        self.PG_esen_entries()
        self.Owner_entries()
        self.PG_login()
        self.check()
       
        self.root.mainloop()

    def PG_entries(self):
        self.PG_heading_frame = Frame(self.root , bg=self.lightgrey_color , width=self.width , height=60)
        self.PG_heading_frame.place(x = 0 , y= 0)
        PG_heading = Label(self.root , text="PG Registration Details" , font=("Arial" , 28 , "bold") , bg= self.lightgrey_color)
        PG_heading.place(x = 480 , y = 5 )

    def Owner_entries(self):
        self.owner_name = Label(self.root , text="Owner Name" , bg= self.color_lightblue , font=self.font)
        self.owner_name.place(x= 20 , y = 90)
        self.owner_entry = Entry(self.root , font=self.font)
        self.owner_entry.place(x = 20 , y= 130)

        # number 
        self.owner_number = Label(self.root , text="Phone Number 1" , bg= self.color_lightblue , font=self.font)
        self.owner_number.place(x= 20 , y = 170)
        self.owner_number_entry = Entry(self.root , font=self.font)
        self.owner_number_entry.place(x = 20 , y= 210)
        # no2
        self.owner_number2 = Label(self.root , text="Phone Number 2 (optional)" , bg= self.color_lightblue , font=self.font)
        self.owner_number2.place(x= 20 , y = 250)
        self.numbe2_entry = Entry(self.root , font=self.font)
        self.numbe2_entry.place(x = 20 , y= 290)

        # address
        self.add_house_name = Label(self.root , text="House Number" , bg= self.color_lightblue , font=self.font)
        self.add_house_name.place(x= 20 , y = 330)
        self.add_house_entry = Entry(self.root , font=("Arial" , 18 ))
        self.add_house_entry.place(x = 20 , y= 360)

        self.add_road_name = Label(self.root , text="Street Name" , bg= self.color_lightblue , font=self.font)
        self.add_road_name.place(x= 20 , y = 400)
        self.add_road_entry = Entry(self.root , font=self.font)
        self.add_road_entry.place(x = 20 , y= 430)

        self.add_city_name = Label(self.root , text="City" , bg= self.color_lightblue , font=self.font)
        self.add_city_name.place(x= 20 , y = 470)
        self.add_city_entry = Entry(self.root , font=self.font)
        self.add_city_entry.place(x = 20 , y= 500)

        self.add_landmark_name = Label(self.root , text="Landmark" , bg= self.color_lightblue , font=self.font)
        self.add_landmark_name.place(x= 20 , y = 540)
        self.add_landmark_entry = Entry(self.root , font=self.font)
        self.add_landmark_entry.place(x = 20 , y= 570)

    def PG_esen_entries(self):
        self.n_college = Label(self.root , text = "Nearby College" , font=self.font,bg="lightblue")
        self.n_college.place(x = 380 , y = 100)
        self.n_college_entry = Entry(self.root , font=self.font )
        self.n_college_entry.place(x = 380 , y = 140)

        # basic pg_room
        self.rooms_avail=Label(self.root,text="Number of Rooms (Available)",font=self.font,bg="lightblue")
        self.rooms_avail.place(x=380,y=180)
        li2= [i for i in range(10)]
        self.room_avail_c=ttk.Combobox(self.root,values=li2 , font= self.font)
        self.room_avail_c.place(x=380,y= 210)
        
        self.wash_avail=Label(self.root,text="Number of WashRooms (Available)",font=self.font,bg="lightblue")
        self.wash_avail.place(x=380,y=260)
        li2= [i for i in range(10)]
        self.wash_avail_c=ttk.Combobox(self.root,values=li2 , font= self.font)
        self.wash_avail_c.place(x=380,y= 290)
        
        self.sharing_pg=Label(self.root,text="Sharing allowed",font=("arial",15,"normal"),bg="lightblue")
        self.sharing_pg.place(x=380,y=330)
        li2= ["yes" , "No", "Other(specify)"]
        self.sharing_pg_entry=ttk.Combobox(self.root,values=li2 , font= self.font)
        self.sharing_pg_entry.place(x=380,y= 360)
        
    def PG_login(self):
        # email
        self.email = Label(self.root , text="Email" , bg= self.color_lightblue , font=self.font)
        self.email.place(x= 380 , y = 400)
        self.email_entry = Entry(self.root , font=self.font)
        self.email_entry.place(x = 380 , y= 430)

        # password
        self.password = Label(self.root , text="Password" , bg= self.color_lightblue , font=self.font)
        self.password.place(x= 380 , y = 470)
        self.password_entry = Entry(self.root , font=self.font , show="*")
        self.password_entry.place(x = 380 , y= 500)

        self.confirm_password = Label(self.root , text="Confirm Password" , bg= self.color_lightblue , font=self.font)
        self.confirm_password.place(x= 380 , y = 540)
        self.confirm_password_entry = Entry(self.root , font=self.font , show="*")
        self.confirm_password_entry.place(x = 380 , y= 570)
        # self.check()

        self.button = Button(self.root , text="Submit" , bg=self.lightgrey_color , width=50 , command=self.getVal)
        self.button.place(x = 750 , y = 300)

    def check(self):
        self.Degree=Label(self.root,text="Price Available",font=("arial",20,"normal"),bg="lightblue")
        self.Degree.place(x=750,y=110)
        var1=IntVar()
        Checkbutton(self.root,text="500-1000",variable=var1).place(x=750,y=170)
        var2=IntVar()
        Checkbutton(self.root,text="1000-1500",variable=var2).place(x=750,y=210)
        var3=IntVar()
        Checkbutton(self.root,text="1500-2000",variable=var3).place(x=750,y=250)
        var4=IntVar()
        Checkbutton(self.root,text="2000-2500",variable=var4).place(x=850,y=170)
        var5=IntVar()
        Checkbutton(self.root,text="2500-3000",variable=var5).place(x=850,y=210)
        var6=IntVar()
        Checkbutton(self.root,text="3000-3500",variable=var6).place(x=850,y=250)
        var7=IntVar()
        Checkbutton(self.root,text="3500-4000",variable=var7).place(x=950,y=170)
        var8=IntVar()
        Checkbutton(self.root,text="4000-4500",variable=var8).place(x=950,y=210)
        var9=IntVar()
        Checkbutton(self.root,text="4500-5000",variable=var9).place(x=950,y=250)
    
    def getVal(self):
        # print("Hi")
        self.password = self.password_entry.get()
        self.name = self.owner_entry.get()
        self.number = self.owner_number_entry.get()
        self.college = self.n_college_entry.get()
        self.email = self.email_entry.get()
        self.room = self.room_avail_c.get()
        self.sharing = self.sharing_pg_entry.get()
        self.landmark = self.add_landmark_entry.get()
        self.city  = self.add_city_entry.get()
        self.address = str(self.add_house_entry.get() + self.add_road_entry.get())
        self.price = 3000
        self.putdata()
    
    def putdata(self):
        data = ( self.name , self.number , self.address  , self.room ,  self.email,
                 self.password , self.price , self.college ,  self.landmark)
        
        print(data)

        



        




        


p1 = PG()