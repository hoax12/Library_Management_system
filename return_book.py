import datetime
import smtplib
import sqlite3
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox, ttk
from datetime import timedelta,date
from datetime import datetime
import pytz
from tkcalendar import *

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
adate=StringVar()
f1 = Frame(root, height=550, width=480, bg='white', borderwidth=7, relief=SOLID)
f1.place(x=425, y=80)
Label2 = Label(f1, text='RETURN BOOK ', font=('goudy old style', 22, 'bold'), fg='black',
               bg='gray98')
Label2.place(x=50, y=15)
l1 = Label(f1, text='Book ID : ', font='goudy_old_style 15 bold', bg='white', fg='black').place(x=50, y=100)
e1 = Entry(f1, width=25, bd=4, bg='orange', textvariable=aidd, borderwidth=2, relief=SOLID).place(x=180, y=100)
l2 = Label(f1, text='Student Id : ', font='goudy_old_style 15 bold', bg='white', fg='black').place(x=50, y=150)
e2 = Entry(f1, width=25, bd=4, bg='orange', textvariable=astudentt, borderwidth=2, relief=SOLID).place(x=180, y=150)
#cal= Calendar(f1, selectmode = 'day',borderwidth=5).place(x=65,y=245)
l4 = Label(f1, text='Date Format -- dd/mm/yyyy ', font='goudy_old_style 10 bold', bg='white', fg='black',).place(x=165, y=235)


#def grab_date():
    #date_label.config(text=cal.get_date())

#b3 = Button(f1, text='Get Date', font='eras_medium_itc 12 bold', fg='black', bg='orange', width=8, bd=3, borderwidth=2,
           # relief=SOLID).place(x=350, y=200)

#l3 = Label(f1, text='Return Date : ', font='goudy_old_style 15 bold', bg='white', fg='black',).place(x=45, y=200)
#e3 = Entry(f1, width=25, bd=4, bg='orange', borderwidth=2,  relief=SOLID, textvariable=adate).place(x=180, y=205)
#date_label = Label(f1, text = "").place(x=200,y=200)

software_version = 'v1.1'
IST = pytz.timezone('Asia/Kolkata')
label_date_now = Label(f1,text="Current Date:", font='goudy_old_style 15 bold', bg='white', fg='black')
label_date_now.place(x=45, y=200)

#label_time_now = Label(f1,text="Current Time :", font = 'Verdana 12')
#label_time_now.place(x=20, y=0)

date_text_var = StringVar()
date_textbox = Entry(f1,width = 25,bd=4, fg= 'black', textvariable = date_text_var,   relief=SOLID, bg='orange', borderwidth=2)
date_textbox['textvariable'] = date_text_var
date_textbox.place(x= 180, y=205)

def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%H:%M:%S %p")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    #label_date_now.config(text = date_now)
    label_date_now.after(500, update_clock)
    #label_time_now.config(text = time_now)
    #label_time_now.after(1000, update_clock)
    return formatted_now

def insert_today_date():
    formatted_now = update_clock()
    date_text_var.set(formatted_now)
    #tomorrow_date_chkbox['state'] = DISABLED

chkbox_today_var = IntVar()
today_date_chkbox = Checkbutton(f1, text='Today',bg='orange',fg='black', font='goudy_old_style 12 bold', variable=chkbox_today_var, onvalue= 1, offvalue=0, command = insert_today_date)
today_date_chkbox.place(x=340, y= 200)

#chkbox_tomorrow_var = IntVar()
#tomorrow_date_chkbox = Checkbutton(f1, text='Tomorrow', variable=chkbox_tomorrow_var, onvalue= 1, offvalue=0, state = DISABLED)
#tomorrow_date_chkbox.place(x= 435, y= 65)

def returnbook():
    a = aidd.get()
    b = astudentt.get()
    c = adate.get()
    con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
    cur = con.cursor()
    cur.execute("select ID from books_info where ID=%s", (a.capitalize(),))
    fh = cur.fetchall()
    con.commit()
    if fh != []:
        con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
        cur = con.cursor()
        cur.execute("select * from book_issued where BOOK_ID=%s and STUDENT_ID=%s",
                    (a.capitalize(), b.capitalize(),))
        d = cur.fetchall()
        con.commit()
        if len(d) != 0:
            con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
            cur = con.cursor()
            cur.execute("DELETE FROM book_issued where BOOK_ID=%s and STUDENT_ID=%s",
                        (a.capitalize(), b.capitalize(),));
            con.commit()
            #cur.execute('UPDATE newbook_issued SET act_returndate=%s, WHERE book_id=%s and STUDENT_ID=%s',
                       # (a.capitalize(), b.capitalize(),));
            #con.commit()

            cur.execute("update books_info set COPIES=COPIES+1 where ID=%s", (a.capitalize()))
            con.commit()

            cur.execute("SELECT email FROM employee1 WHERE user_id=%s", (b.capitalize()))
            var = cur.fetchone()
            str = ''.join(var)
            print(str)
            msg = EmailMessage()
            msg['Subject'] = 'Book issued from 24/7 Library'
            msg['From'] = '24/7 Library'
            msg["To"] = str
            msg.set_content("""LIBRARY DEPARTMENT
                                    Library Return Books Department
                                    Hello Your book has been Returned to our library
                                    Thank you for Issuing and Returning the book from our library""")
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('rajneeshpaul12@gmail.com', 'rajneesh@12')
            server.send_message(msg)
            server.quit()
            con.close()

            messagebox.showinfo("Success", "Book Returned sucessfully.")
        else:
            messagebox.showinfo("Error", "Data not found.")

    else:
        messagebox.showinfo("Error", "No such book.\nPlease add the book in database.")
    con.commit()
    con.close()


b1 = Button(f1, text='Return', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=10, bd=3,
            borderwidth=2, relief=SOLID,command=returnbook).place(x=200, y=300)


def back():
    root.destroy()
    import adminlogin3



b1 = Button(f1, text='Back', font='eras_medium_itc 14 bold', fg='black', bg='orange', width=10, bd=3, borderwidth=2,
            relief=SOLID, command=back).place(x=50, y=300)








root.maxsize(1350, 710)
root.minsize(1350, 710)

root.mainloop()