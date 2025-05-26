import datetime
import smtplib
import sqlite3
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox, ttk
from datetime import timedelta,date


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

f1 = Frame(root, height=550, width=500, bg='white', borderwidth=7, relief=SOLID)
f1.place(x=425, y=80)
Label2 = Label(f1, text='ISSUE BOOK ', font=('goudy old style', 22, 'bold'), fg='black',
               bg='gray98')
Label2.place(x=30, y=15)
l1 = Label(f1, text='Book ID : ', font='goudy_old_style 15 bold', bg='white', fg='black').place(x=50, y=100)
e1 = Entry(f1, width=25, bd=4, bg='orange', textvariable=aidd, borderwidth=2, relief=SOLID).place(x=180, y=100)
l2 = Label(f1, text='Student Id : ', font='goudy_old_style 15 bold', bg='white', fg='black').place(x=50, y=150)
e2 = Entry(f1, width=25, bd=4, bg='orange', textvariable=astudentt, borderwidth=2, relief=SOLID).place(x=180, y=150)


def issuedbook():
    bookid = aidd.get()
    studentid = astudentt.get()
    issue_date = (date.today())
    r=timedelta(days=90)
    return_date = issue_date + r
    return_date1= (return_date)
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    cur.execute("select id,copies from books_info where id=%s",bookid.capitalize())
    an = cur.fetchall()
    if (bookid and studentid != ""):
        if an != []:
            for i in an:
                if i[:1] != 0:
                    try:
                        con = pymysql.connect(host='localhost', user='root', password='Sid@1234',
                                              database='myprojectdb')
                        cur = con.cursor()
                        cur.execute ('insert into book_issued(book_id,student_id,issue_date,return_date) values(%s,%s,%s,%s)',(bookid.capitalize(),studentid.capitalize(),issue_date,return_date1));
                        con.commit()
                        cur.execute("update books_info set COPIES=COPIES-1 where id=%s",bookid.capitalize())
                        con.commit()
                       # cur2.execute('insert into newbook_issued(book_id,student_id,issue_date,return_date) values(%s,%s,%s,%s)',(bookid.capitalize(), studentid.capitalize(), issue_date, return_date1));
                        #con.commit()
                        cur.execute("SELECT email FROM employee1 WHERE user_id=%s",(studentid.capitalize()))
                        var = cur.fetchone()
                        str = ''.join(var)
                        print(str)
                        msg = EmailMessage()
                        msg['Subject'] = 'Book issued from 24/7 Library'
                        msg['From'] = '24/7 Library'
                        msg["To"] = str
                        msg.set_content("""LIBRARY DEPARTMENT
                        Library Issued Books Department
                        Hello Your book has been Issued from our library
                        Thank you for Issuing the book from our library""")
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('rajneeshpaul12@gmail.com', 'rajneesh@12')
                        server.send_message(msg)
                        server.quit()
                        con.close()
                        messagebox.showinfo("Updated", "Book Issued sucessfully.")

                    except Exception as e:
                        messagebox.showinfo("Error", f"Error Due TO:{e}.")

                else:
                    messagebox.showinfo("Unavailable", "Book unavailable.\nThere are 0 copies of the book.")
        else:
            messagebox.showinfo("Error", "No such Book in Database.")
    else:
        messagebox.showinfo("Error", "Fields cannot be blank.")

'''
def send_mail():
    bookid = aidd.get()
    studentid = astudentt.get()
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    cur.execute("SELECT email FROM employee1 WHERE user_id=%s", (bookid.capitalize()))
    var3 = cur.fetchone()
    str = ''.join(var3)
    print(str)
    msg = EmailMessage()
    msg['Subject'] = 'Book issued from 24/7 Library'
    msg['From'] = '24/7 Library'
    msg["To"] = str
    msg.set_content("""LIBRARY DEPARTMENT
                            Library Issued Books Department
                            Hello Your book has been Issued from our library
                            Thank you for Issuing the book from our library""")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('rajneeshpaul12@gmail.com', 'rajneesh@12')
    server.send_message(msg)
    server.quit()'''




b1 = Button(f1, text='Issue', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=10, bd=3,
            borderwidth=2, relief=SOLID,command=issuedbook).place(x=200, y=250)

#b2 = Button(f1, text='Send Mail', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=10, bd=3,
        #    borderwidth=2, relief=SOLID,command=send_mail).place(x=350, y=250)


def back():
    root.destroy()
    import adminlogin3



b1 = Button(f1, text='Back', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=10, bd=3, borderwidth=2,
            relief=SOLID, command=back).place(x=50, y=250)


root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()