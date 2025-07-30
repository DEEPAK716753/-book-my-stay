import tkinter
from tkintermapview import TkinterMapView
import getlongi
import customtkinter as ctk

class Map:
    def __init__(self, details):
        self.root_tk = ctk.CTkToplevel()
        self.root_tk.geometry(f"{600}x{400}")
        self.details = details
        self.address = getlongi.get_coordinates(self.details)
        print("----", self.address)
        self.root_tk.title(f"{self.details}")
        
        self.root_tk.lift()
        self.root_tk.focus_set()
        # Create map widget
        self.map_widget = TkinterMapView(self.root_tk, width=600, height=400, corner_radius=0)
        self.map_widget.pack(fill="both", expand=True)

        # Set the map position
        if self.address:
            self.map_widget.set_position(self.address[0], self.address[1], marker=True)
            self.map_widget.set_zoom(17)
        else:
            print("Address coordinates could not be found.")

        self.root_tk.mainloop()

if __name__ == "__main__":
    obj = Map('Jalandhar bus stand')
