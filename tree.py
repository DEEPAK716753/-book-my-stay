from tkinter import *
from tkinter import ttk
import database


class All:
    def __init__(self):
        screen= Tk()
        screen.title("All User")
        screen.geometry('600x300')
        table= ttk.Treeview(screen, columns=["id",'Name','Email','Password','a','c'], show='headings')

        table.heading('#1',text="Id")
        table.heading('#2',text="Name")
        table.heading('#3',text="Email")
        table.heading('#4',text="Password")
        table.heading('#5',text="Edit")
        table.heading('#6',text="Delete")
        table.column("#1",width=80)
        table.column("#2",width=100)
        table.column("#3",width=140)
        table.column("#4",width=100)
        table.column("#5",width=70)
        table.column("#6",width=70)

        res= database.getAllUsers()
        # print(res)


        for i in res:
            print(i)
            table.insert('',5,text=i[0],values=(i[0],i[1],i[2],i[3],'Edit','Delete'))
            
        table.pack()



        screen.mainloop()


if __name__ == "__main__":
    obj1 = All()
