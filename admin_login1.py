import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql


def book_data():
    root.destroy()
    import adminlogin2

def std_data():
    root.destroy()
    import adminlogin3


def logout():
    MsgBox = tkinter.messagebox.askquestion('Exit Application', 'Do You Really want to Logout?', )
    if MsgBox == 'yes':
        root.destroy()
        import login
    else:
        pass


root = Tk()
root.geometry('1350x710+0+10')
root.title('Library Management System')
bg = PhotoImage(file='bgpic1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)

frame = Frame(root, width=760, height=160, borderwidth=10, relief=SOLID, background='gray98')
frame.place(x=295, y=245)
frame1 = Frame(root, width=900, height=114, borderwidth=10, relief=SOLID, background='gray98')
frame1.place(x=220, y=5)
nameLabel = Label(frame1, text=' WELCOME TO THE  24/7 LIBRARY', font=('Kristen itc', 33, 'bold'), fg='black',
                                        bg='gray98')
nameLabel.place(x=10, y=10)

bookbutton2 = Button(root, width=13, text='Book Data', font=('eras medium itc', 28, 'bold'), fg='white', bg='gray20',
                     cursor='hand2',
                     background='gray20', foreground='white', borderwidth=5, relief=SOLID, command=book_data)
bookbutton2.place(x=710, y=285)
studentbutton1 = Button(root, width=13, text='Student Data', font=('eras medium itc', 28, 'bold'), fg='white',
                        bg='black', cursor='hand2',
                        background='gray20', foreground='white', borderwidth=5, relief=SOLID,command=std_data)
studentbutton1.place(x=325, y=285)

logoutbutton1 = Button(root, width=18, text='Logout', font=('eras medium itc', 22, 'bold'), fg='white', bg='black',
                       cursor='hand2',
                       background='white', foreground='gray20', borderwidth=6, relief=SOLID, command=logout)
logoutbutton1.place(x=1028, y=645)

root.maxsize(1350, 710)
root.minsize(1350, 710)
root.mainloop()
