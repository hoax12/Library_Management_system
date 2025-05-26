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
Label2 = Label(f1, text='ALL AVAILABLE BOOKS ', font=('goudy old style', 22, 'bold'), fg='black',bg='gray98')
Label2.place(x=30, y=15)

l1 = Label(f1, text='Title / Author: ', font=('goudy_old_style 14 bold'), bd=2, fg='black',
               bg='white').place(x=40, y=75)
e1 = Entry(f1, width=28, bd=10, bg='orange', font=('times new roman', 15), fg='black', textvariable=sid1,
               borderwidth=2, relief=SOLID).place(x=180, y=75)

my_tree = ttk.Treeview(f1)
my_tree['columns'] = ("Book ID", "Title", "Author", "Genre", "Copies","Location")

my_tree.column("#0", width=0,stretch=NO)
my_tree.column("Book ID", anchor=W, width=70)
my_tree.column("Title", anchor=CENTER, width=120)
my_tree.column("Author", anchor=W, width=120)
my_tree.column("Genre", anchor=W, width=120)
my_tree.column("Copies", anchor=W, width=80)
my_tree.column("Location", anchor=W, width=80)
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Book ID", text="Book ID", anchor=W)
my_tree.heading("Title", text="Title", anchor=W)
my_tree.heading("Author", text="Author", anchor=W)
my_tree.heading("Genre", text="Genre", anchor=W)
my_tree.heading("Copies", text="Copies", anchor=W)
my_tree.heading("Location", text="Location", anchor=W)
my_tree.place(x=30, y=125)

def search():
     k = sid1.get()
     try:
        if k!="":
         con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
         cur = con.cursor()
         cur.execute("select * from books_info where name=%s or author=%s",(k.capitalize()))
         g = cur.fetchall()
         if len(g) !=0:
               for row in g:
                my_tree.insert('', END, values=row)
                con.commit()
                con.close()
         else:
             messagebox.showinfo("Error", "Data not found")
        else:
              messagebox.showinfo("Error", "Search field cannot be empty.")
     except Exception as e:
          showerror('Error', f"Error due to: {e}", parent=root)



def all_search():
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234',
                          database='myprojectdb')
    cur = con.cursor()
    try:
        cur.execute("select * from books_info")
        d = cur.fetchall()
        for row in d:
            my_tree.insert("", END, values=row)

        con.commit()

    except Exception as e:
        messagebox.showinfo({e})
    con.close()




def back():
    root.destroy()
    import adminlogin2

b1 = Button(f1, text='Search', bg='orange', font='eras_medium_itc 14 bold', width=8, bd=2, borderwidth=2,relief=SOLID, command=search).place(x=400, y=400)
b2 = Button(f1, text='Back', bg='orange', font='eras_medium_itc 14 bold', width=8, bd=2, borderwidth=2,relief=SOLID, command=back).place(x=100, y=400)
b3 = Button(f1, text='All Books', bg='orange', font='eras_medium_itc 14 bold', width=8, bd=2, borderwidth=2,relief=SOLID, command=all_search).place(x=250, y=400)

style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",background="silver",fieldbackground="silver",foreground="black")
style.map('Treeview',background=[('selected','orange')])
root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()