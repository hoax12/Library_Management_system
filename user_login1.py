import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import showerror

import pymysql

root = Tk()
root.geometry()
root.geometry('1350x710+0+10')
root.title('Library Management System')

def logout():
    MsgBox = tkinter.messagebox.askquestion('Exit Application', 'Do You Really want to Logout?', )
    if MsgBox == 'yes':
        root.destroy()
        import user_login
    else:
        pass

def add_book():
    root.destroy()
    import userbook_data


def search():
 root.destroy()
 import  user_request_book


def view_books():
    root.destroy()
    import user_view_book


def all():
  root.destroy()
  import all_books



def grievance():
    root.destroy()
    import raise_grievance


bg = PhotoImage(file='bgpic1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)
registerFrame = Frame(root, bg='gray98', width=350, height=710, borderwidth=15, relief=SOLID)
registerFrame.place(x=0, y=0)

frame1 = Frame(root, width=1015, height=114, borderwidth=15, relief=SOLID, background='gray98')
frame1.place(x=335, y=0)
nameLabel = Label(frame1, text=' WELCOME TO THE  24/7 LIBRARY', font=('Kristen itc', 33, 'bold'), fg='black',
                                        bg='gray98')
nameLabel.place(x=70, y=10)

forgetpassLabel = Label(root, text='USER DATA', font=('Kristen itc', 30, 'bold'), fg='black',
                        bg='gray98')
forgetpassLabel.place(x=20, y=30)

bookbutton1 = Button(root, width=13, text='Book Data', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID,command=add_book )
bookbutton1.place(x=50, y=150)

requestbutton1 = Button(root, width=13, text='Request Books', font=('eras medium itc', 18, 'bold'), fg='white',
                       bg='black', cursor='hand2',
                       background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=search)
requestbutton1.place(x=50, y=250)

viewbooks = Button(root, width=13, text='View Books', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=view_books)
viewbooks.place(x=50, y=350)

grievancebutton1 = Button(root, width=13, text='Raise Grievance', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=grievance)
grievancebutton1.place(x=50, y=450)


logoutbutton1 = Button(root, width=13, text='Logout', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                       cursor='hand2',
                       background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=logout)
logoutbutton1.place(x=50, y=550)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()
