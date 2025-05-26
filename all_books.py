import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import showerror

import pymysql

root = Tk()
root.geometry()
root.geometry('1350x710+0+10')
root.title('Library Management System')

bg = PhotoImage(file='bgpic1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)
sid1 = StringVar()
f1 = Frame(root, height=500, width=650, bg='white', borderwidth=8, relief=SOLID)
f1.place(x=360, y=100)

Label1 = Label(f1, text='ALL BOOKS ', font=('goudy old style', 22, 'bold'), fg='black',
                            bg='gray98')
Label1.place(x=24, y=28)

my_tree = ttk.Treeview(f1)
my_tree['columns'] = ("Book ID", "Title", "Author", "Genre", "Copies", "Location")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Book ID", anchor=W, width=50)
my_tree.column("Title", anchor=CENTER, width=120)
my_tree.column("Author", anchor=W, width=120)
my_tree.column("Genre", anchor=W, width=140)
my_tree.column("Copies", anchor=W, width=80)
my_tree.column("Location", anchor=W, width=80)
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Book ID", text="Book ID", anchor=W)
my_tree.heading("Title", text="Title", anchor=W)
my_tree.heading("Author", text="Author", anchor=W)
my_tree.heading("Genre", text="Genre", anchor=W)
my_tree.heading("Copies", text="Copies", anchor=W)
my_tree.heading("Location", text="Location", anchor=W)
style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",background="silver",fieldbackground="silver",foreground="black"
                    )
style.map('Treeview',background=[('selected','orange')])
my_tree.place(x=20, y=75)
con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
cur = con.cursor()
cur.execute("select * from books_info")
g = cur.fetchall()
if len(g) != 0:
    for row in g:
        my_tree.insert('', END, values=row)
con.commit()
con.close()

def back():
    root.destroy()
    import adminlogin2

b1 = Button(f1, text='Back', font='eras_medium_itc 14  bold', bg='orange', fg='black', width=10, bd=3,
            borderwidth=2, relief=SOLID, command=back).place(x=250, y=410)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()