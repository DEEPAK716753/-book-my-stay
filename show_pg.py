from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import database
import edit_pg


class viewAddPG():
    # constructor
    def __init__(self, window):
        self.root = window

    def managePG(self):
        self.fr = Frame(self.root, bg="Grey")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0', text="Id")
        self.tr.column('#0', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#1', text="PG")
        self.tr.column('#1', minwidth=0, width=130, stretch=NO)

        self.tr.heading('#2', text="Address")
        self.tr.column('#2', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#3', text="Rent")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="Amenities")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#5', text="Type")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#6', text="Contact")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#7', text="Edit")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#8', text="Delete")
        self.tr.column('#8', minwidth=0, width=80, stretch=NO)

        data = database.allPG()
        print(data)
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1], i[2],i[3],i[4],i[5],i[6], 'Edit', 'Delete'))
        
 
      
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=500,width=800)
        self.root.mainloop()
    


    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        print(gup)
       
        if col == '#8':
            response = messagebox.askyesno('Delete','Do you really want to delete?')
            if response:
                a = database.deletePg(gup)
                if a:
                    messagebox.showinfo('Success', 'task deleted successfully.')
                    # obj = viewAddTask(self.root)
                    # obj.manageTask()
                else:
                    messagebox.showinfo('Alert', 'Something went wrong.')

        if col =="#7":
            message= messagebox.askyesno("Edit","Do you want to edit this?")
            if message:
                obj=edit_pg.EditPG(self.root,gup)
                obj.editSection()
            
            # obj = edittask.createEditTask(self.root)
            # obj.firstFrame(gup)




if __name__ == '__main__':
    obj = viewAddPG
    obj.managePG()
        
            