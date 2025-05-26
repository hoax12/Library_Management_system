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
        import login
    else:
        pass

def add_book():
    root.destroy()
    import add_books


def search():
 root.destroy()
 import  search_books



def all():
  root.destroy()
  import all_books


def back_button():
    root.destroy()
    import admin_login1


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

forgetpassLabel = Label(root, text='BOOK DATA', font=('Kristen itc', 30, 'bold'), fg='black',
                        bg='gray98')
forgetpassLabel.place(x=20, y=30)

addbutton1 = Button(root, width=13, text='Add Books', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=add_book)
addbutton1.place(x=50, y=150)

searchbutton1 = Button(root, width=13, text='Search Books', font=('eras medium itc', 18, 'bold'), fg='white',
                       bg='black', cursor='hand2',
                       background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=search)
searchbutton1.place(x=50, y=250)

allbutton1 = Button(root, width=13, text='All Books', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=all)
allbutton1.place(x=50, y=350)

menubutton1 = Button(root, width=13, text='Back', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                     cursor='hand2',
                     background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=back_button)
menubutton1.place(x=50, y=450)

logoutbutton1 = Button(root, width=13, text='Logout', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                       cursor='hand2',
                       background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=logout)
logoutbutton1.place(x=50, y=550)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()
