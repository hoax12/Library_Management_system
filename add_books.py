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

Label1 = Label(f1, text='ADD BOOKS ', font=('goudy old style', 24, 'bold'), fg='black',
                            bg='gray98')
Label1.place(x=45, y=20)

aid = StringVar()
aauthor = StringVar()
aname = StringVar()
acopies = StringVar()
agenre = StringVar()
aloc = StringVar()

l1 = Label(f1, text='Book ID : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=80)
e1 = Entry(f1, width=30, bg='orange', font=('times new roman', 15), fg='black', textvariable=aid, borderwidth=2,
           relief=SOLID).place(x=150, y=80)
l2 = Label(f1, text='Title : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=130)
e2 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=aname, borderwidth=2,
           relief=SOLID).place(x=150, y=130)
l3 = Label(f1, text='Author : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=180)
e3 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=aauthor, borderwidth=2,
           relief=SOLID).place(x=150, y=180)
l4 = Label(f1, text='Genre : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=230)
e4 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=agenre, borderwidth=2,
           relief=SOLID).place(x=150, y=230)
l4 = Label(f1, text='Copies : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=280)
e5 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=acopies, borderwidth=2,
           relief=SOLID).place(x=150, y=280)
l5 = Label(f1, text='Location : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50,
                                                                                                         y=330)
e6 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=aloc, borderwidth=2,
           relief=SOLID).place(x=150, y=330)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)


def add_book():
    a = aid.get()
    b = aname.get()
    c = aauthor.get()
    d = agenre.get()
    e = acopies.get()
    f = aloc.get()
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    try:

        if (a and b and c and d and f) == "":
            messagebox.showinfo("Error", "Fields cannot be empty.")
        else:
            cur.execute('insert into books_info(id,name,author,genre,copies,location) values(%s,%s,%s,%s,'
                        '%s,%s)',
                        (aid.get(), aname.get(), aauthor.get(), agenre.get(),
                         acopies.get(),
                         aloc.get()))

            con.commit()



            messagebox.showinfo("Success", "Book added successfully")
    except Exception as e:
        showerror('Error', f"Error due to: {e}", parent=root)

    con.close()

def back():
    root.destroy()
    import adminlogin2


b1 = Button(f1, text='Add', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=add_book ).place(x=60, y=400)
b2 = Button(f1, text='Back', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=back).place(x=400, y=400)

def delete_book():
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    try:
            cur.execute('delete from books_info where id=%s',
                        (aid.get()))

            con.commit()

            messagebox.showinfo("Success", "Book Deleted successfully")
    except Exception as e:
        showerror('Error', f"Error due to: {e}", parent=root)

    con.close()


b3 = Button(f1, text='Delete', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=delete_book).place(x=230, y=400)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()