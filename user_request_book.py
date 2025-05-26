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

Label1 = Label(f1, text='REQUEST BOOKS ', font=('goudy old style', 24, 'bold'), fg='black',
                            bg='gray98')
Label1.place(x=45, y=20)

std_id = StringVar()
std_name= StringVar()
b_name = StringVar()
author = StringVar()
Date = StringVar()
Comments=StringVar()

l1 = Label(f1, text='Student ID : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=80)
e1 = Entry(f1, width=30, bg='orange', font=('times new roman', 15), fg='black', textvariable=std_id, borderwidth=2,
           relief=SOLID).place(x=150, y=80)
l2 = Label(f1, text='Name : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=130)
e2 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=std_name, borderwidth=2,
           relief=SOLID).place(x=150, y=130)
l3 = Label(f1, text='Book Title : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=180)
e3 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=b_name, borderwidth=2,
           relief=SOLID).place(x=150, y=180)
l4 = Label(f1, text='Author : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=230)
e4 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=author, borderwidth=2,
           relief=SOLID).place(x=150, y=230)
l5 = Label(f1, text='Date : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=280)
e5 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=Date, borderwidth=2,
           relief=SOLID).place(x=150, y=280)
l6 = Label(f1, text='Comments : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50,
                                                                                                         y=330)
e6 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=Comments, borderwidth=2,
           relief=SOLID).place(x=150, y=330)


def request_book():
    a = std_id.get()
    b = std_name.get()
    c = b_name.get()
    d = author.get()
    e = Date.get()
    f = Comments.get()
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    try:

        if (a and b and c and d and f) == "":
            messagebox.showinfo("Error", "Fields cannot be empty.")
        else:
            cur.execute('insert into request_book(student_id,std_name,book_title,author,date,Comments) values(%s,%s,%s,%s,'
                        '%s,%s)',
                        (std_id.get(), std_name.get(), b_name.get(), author.get(),
                         Date.get(),
                         Comments.get()))

            con.commit()

            messagebox.showinfo("Success", "Request Sent Successfully")
    except Exception as e:
        showerror('Error', f"Error due to: {e}", parent=root)

    con.close()

def back():
    root.destroy()
    import user_login1


b1 = Button(f1, text='Request', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=request_book).place(x=60, y=400)
b2 = Button(f1, text='Back', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=back).place(x=270, y=400)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()