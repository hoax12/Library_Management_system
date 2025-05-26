import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

import pymysql

root = Tk()
root.geometry()
root.geometry('1350x710+0+10')
root.title('Library Management System')




def issue():
 root.destroy()
 import issue_book

def returnn():
   root.destroy()
   import return_book

def activity():
    root.destroy()
    import std_activity


def back_button():
    root.destroy()
    import admin_login1

def view_request():
    root.destroy()
    import book_request_admin

def view_grievance():
    root.destroy()
    import view_grievance_admin


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

forgetpassLabel = Label(root, text='STUDENT DATA', font=('Kristen itc', 24, 'bold'), fg='black',
                        bg='gray98')
forgetpassLabel.place(x=20, y=30)

issuebutton1 = Button(root, width=13, text='Issue Book', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=issue)
issuebutton1.place(x=50, y=120)

returnbutton1 = Button(root, width=13, text='Return Book', font=('eras medium itc', 18, 'bold'), fg='white',
                       bg='black', cursor='hand2',
                       background='gray30', foreground='white', borderwidth=5, relief=SOLID,command=returnn)
returnbutton1.place(x=50, y=200)

actbutton1 = Button(root, width=13, text='Student Activity', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                    cursor='hand2',
                    background='gray30', foreground='white', borderwidth=5, relief=SOLID,command=activity)
actbutton1.place(x=50, y=280)

requestbutton1 = Button(root, width=13, text='Book Request', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                     cursor='hand2',
                     background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=view_request)
requestbutton1.place(x=50, y=360)

grievancebutton1 = Button(root, width=13, text='View Grievance', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                     cursor='hand2',
                     background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=view_grievance)
grievancebutton1.place(x=50, y=440)

menubutton1 = Button(root, width=13, text='Back', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                     cursor='hand2',
                     background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=back_button)
menubutton1.place(x=50, y=520)



logoutbutton1 = Button(root, width=13, text='Logout', font=('eras medium itc', 18, 'bold'), fg='white', bg='black',
                     cursor='hand2',
                     background='gray30', foreground='white', borderwidth=5, relief=SOLID, command=back_button)
logoutbutton1.place(x=50, y=600)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()
