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

Label1 = Label(f1, text='RAISE GRIEVANCE ', font=('goudy old style', 24, 'bold'), fg='black',
                            bg='gray98')
Label1.place(x=45, y=20)

std_id= StringVar()
name1 = StringVar()
date = StringVar()
Commment = StringVar()


l1 = Label(f1, text='Student ID : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=100)
e1 = Entry(f1, width=30, bg='orange', font=('times new roman', 15), fg='black', textvariable=std_id, borderwidth=2,
           relief=SOLID).place(x=150, y=100)
l2 = Label(f1, text='Name: ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=150)
e2 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=name1, borderwidth=2,
           relief=SOLID).place(x=150, y=150)
l3 = Label(f1, text='Date : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=200)
e3 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=date, borderwidth=2,
           relief=SOLID).place(x=150, y=200)
l4 = Label(f1, text='Comment : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=250)
e4 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=Commment, borderwidth=2,
           relief=SOLID).place(x=150, y=250)

#comment = Text(f1, width=27, height=5, font=('Arial', 14), bg='orange', borderwidth=2,text=Commment,
          # relief=SOLID)
#comment.place(x=150,y=230)

'''l4 = Label(f1, text='Copies : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50, y=280)
e5 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=acopies, borderwidth=2,
           relief=SOLID).place(x=150, y=280)'''
'''l5 = Label(f1, text='Location : ', font='goudy_old_style 12 bold', fg='black', bg='white', pady=1).place(x=50,
                                                                                                         y=330)
e6 = Entry(f1, width=30, bg='orange', fg='black', font=('times new roman', 15), textvariable=aloc, borderwidth=2,
           relief=SOLID).place(x=150, y=330)'''


def add_book():
    a = std_id.get()
    b = name1.get()
    c = date.get()
    d = Commment.get()
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    try:

        if (a and b and c and d) == "":
            messagebox.showinfo("Error", "Fields cannot be empty.")
        else:
            cur.execute('insert into grievance_user(Std_ID,Name,Date,Comment) values(%s,%s,%s,%s)',
                        (std_id.get(), name1.get(), date.get(), Commment.get(),))

            con.commit()

            messagebox.showinfo("Success", "Grievance Raised Successfully")
    except Exception as e:
        showerror('Error', f"Error due to: {e}", parent=root)

    con.close()

def back():
    root.destroy()
    import user_login1


b1 = Button(f1, text='Submit', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=add_book ).place(x=60, y=350)
b2 = Button(f1, text='Back', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=12, bd=3, borderwidth=2,
            relief=SOLID,command=back).place(x=270, y=350)

root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()