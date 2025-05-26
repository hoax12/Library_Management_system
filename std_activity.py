import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

import pymysql

root = Tk()
root.geometry()
root.geometry('1350x710+0+10')
root.title('Library Management System')
bg = PhotoImage(file='bgpic1.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)

aidd = StringVar()
astudentt = StringVar()
f1 = Frame(root, height=550, width=500, bg='white' ,borderwidth=7 ,relief=SOLID)
f1.place(x=425, y=80)
Label2 = Label(f1, text='STUDENT ACTIVITY ', font=('goudy old style', 22, 'bold'), fg='black',
               bg='gray98')
Label2.place(x=30, y=15)

list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
    #trees = create_tree(f1, list2)
    #trees.place(x=50, y=150)

l1 = Label(f1, text='Book/Student ID : ', font='goudy_old_style 15 bold', fg='black', bg='white').place(x=32, y=100)
e1 = Entry(f1, width=15, bd=10, bg='orange',font="times_new_roman,6,bold", textvariable=aidd,borderwidth=2,relief=SOLID).place(x=222, y=100)
    # l2=Label(self.f1,text='Student Id : ',font='papyrus 15 bold',fg='orange',bg='black').place(x=50,y=80)
    # e2=Entry(self.f1,width=20,bd=4,bg='orange',textvariable=self.astudentt).place(x=180,y=80)

my_tree = ttk.Treeview(f1)
my_tree['columns'] = ("Book ID","Student ID","Issue Date","Return Date")

my_tree.column("#0", width=0,stretch=NO)
my_tree.column("Book ID", anchor=W, width=70)
my_tree.column("Student ID", anchor=CENTER, width=120)
my_tree.column("Issue Date", anchor=W, width=120)
my_tree.column("Return Date", anchor=W, width=120)
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Book ID", text="Book ID", anchor=W)
my_tree.heading("Student ID", text="Student ID", anchor=W)
my_tree.heading("Issue Date", text="Issue Date", anchor=W)
my_tree.heading("Return Date", text="Return Date", anchor=W)
my_tree.place(x=30, y=155)
style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",background="silver",fieldbackground="silver",foreground="black")
style.map('Treeview',background=[('selected','orange')])

def back():
  root.destroy()
  import  adminlogin3

def search_all():
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234',
                          database='myprojectdb')
    cur = con.cursor()
    try:
        cur.execute("select * from book_issued")
        d = cur.fetchall()
        for row in d:
            my_tree.insert("", END, values=row)


        con.commit()

    except Exception as e:
        messagebox.showinfo({e})
    con.close()

def search_act():
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234',
                          database='myprojectdb')
    cur = con.cursor()

    bid = aidd.get()
    if aidd !=0:
        try:
            cur.execute("select * from book_issued where BOOK_ID=%s or STUDENT_ID=%s",
                        (bid.capitalize(), bid.capitalize(),))
            d = cur.fetchall()
            if len(d) != 0:
                for row in d:
                    my_tree.insert("", END, values=row)
            else:
                messagebox.showinfo("Error", "Data not found.")
            con.commit()

        except Exception as e:
            messagebox.showinfo(e)
            con.close()
    else:
        messagebox.showinfo("Error","Search Fields cannot be Blank")


b1 = Button(f1, text='Search', bg='orange', font='eras_medium_itc 14 bold', width=10, bd=3,borderwidth=2,relief=SOLID,command=search_act ).place(x=340,y=450)
b1 = Button(f1, text='Back', bg='orange', font='eras_medium_itc 14 bold', width=10, bd=3,borderwidth=2,relief=SOLID,command=back).place(x=40, y=450)
b1 = Button(f1, text='All', bg='orange', font='eras_medium_itc 14 bold', width=10, bd=3,borderwidth=2,relief=SOLID,command=search_all ).place(x=190, y=450)




root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()