from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql


def back_command():
    root.destroy()
    import log_modules


def forget_password():
    def reset():
        securityquescombo.current(0)
        newpassEntry.delete(0, END)
        answerforgetEntry.delete(0, END)
        mailentry.delete(0, END)
        passentry.delete(0, END)


    def reset_password():
        if securityquescombo.get() == 'Select' or answerforgetEntry.get() == '' or newpassEntry.get() == '':
            showerror('Error', 'All Fields Are Required', parent=root2)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
                cur = con.cursor()
                cur.execute('select * from employee1 where email=%s and question=%s and answer=%s',
                            (mailentry.get(), securityquescombo.get(), answerforgetEntry.get()))
                row = cur.fetchone()
                if row == None:
                    showerror('Error', 'Security Question or Answer is Incorrect\n\n\tPlease Try Again ', parent=root2)

                else:
                    cur.execute('update employee1 set password=%s where email=%s',
                                (newpassEntry.get(), mailentry.get()))
                    con.commit()
                    con.close()
                    showinfo('Success', 'Password is reset, please login with new password', parent=root2)
                    reset()
                    root2.destroy()


            except Exception as e:
                showerror('Error', f"Error due to: {e}", parent=root)

    if mailentry.get() == '':
        showerror('Error', 'Please enter the Email Address to reset your Password', parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
            cur = con.cursor()
            cur.execute('select * from employee1 where email=%s', mailentry.get())
            row = cur.fetchone()
            if row == None:
                showerror('Error', 'Please enter the valid email address', parent=root)

            else:
                con.close()
                root2 = Toplevel()
                root2.title('Forget Password')
                root2.geometry('470x560+400+60')
                root2.config(bg='white')
                root2.focus_force()
                root2.grab_set()
                root2.maxsize(470,560)
                root2.minsize(470,560)
                passwordimage = PhotoImage(file='forgotpwdimg.png')
                forgetimageLabel = Label(root2, image=passwordimage, bg='white')
                forgetimageLabel.place(x=0, y=0)
                forgetLabel = Label(root2, text='Forget', font=('times new roman', 22, 'bold'), fg='black')
                forgetLabel.place(x=128, y=28)
                forgetpassLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), fg='green')

                forgetpassLabel.place(x=225, y=28)

                securityquesLabel = Label(root2, text='Security Questions', font=('times new roman', 19, 'bold'),
                                          fg='black')
                securityquesLabel.place(x=60, y=160)
                securityquescombo = ttk.Combobox(root2, font=('times new roman', 19), state='readonly', justify=CENTER,
                                                 width=28)
                securityquescombo['values'] = (
                    'Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                    'Your Favourite Teacher?', 'Your Favourite Hobby?')
                securityquescombo.place(x=60, y=200)
                securityquescombo.current(0)

                answerforgetLabel = Label(root2, text='Answer', font=('times new roman', 19, 'bold'), fg='black')

                answerforgetLabel.place(x=60, y=245)
                answerforgetEntry = Entry(root2, font=('times new roman', 19,), fg='black', width=30,borderwidth=1,relief=SOLID)

                answerforgetEntry.place(x=60, y=284)
                pwd=StringVar()
                newpassLabel = Label(root2, text='New Password', font=('times new roman', 19, 'bold'), fg='black')

                newpassLabel.place(x=60, y=330)
                newpassEntry = Entry(root2, font=('times new roman', 19,), fg='black', width=30,
                                     bg='white',borderwidth=1,relief=SOLID,textvariable=pwd,show='*')
                newpassEntry.place(x=60, y=370)

                changepassbutton = Button(root2, text='Change Password', font=('arial', 17, 'bold'), bg='green',
                                          fg='white', cursor='hand2', activebackground='green',
                                          activeforeground='white',
                                          command=reset_password,borderwidth=3,relief=SOLID)
                changepassbutton.place(x=200, y=415)

                root2.mainloop()

        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


def register_window():
    root.destroy()
    import user_register


def signin():
    a=mailentry.get()
    with open('pass.txt', 'w') as f:
     f.write(a)
    if mailentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
            cur = con.cursor()
            cur.execute('select * from employee1 where user_id=%s and password=%s', (mailentry.get(), passentry.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid User ID or Password')


            else:
                root.destroy()
                import user_login1


            con.close()
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


root = Tk()
root.geometry('900x600+50+50')
root.title('Library Management System')
bglogin = PhotoImage(file='bgpic.png')
bgloginLabel = Label(root, image=bglogin)
bgloginLabel.place(x=0, y=0)

frame = Frame(root, bg='gray98', width=560, height=320,borderwidth=5,relief=SOLID)
frame.place(x=180, y=140)

userimage = PhotoImage(file='picuser.png')
userimageLabel = Label(frame, image=userimage, bg='white')
userimageLabel.place(x=10, y=30)
mailLabel = Label(frame, text='User ID', font=('goudy old style', 22, 'bold'), bg='white', fg='black')
mailLabel.place(x=220, y=32)
mailentry = Entry(frame, font=('arial', 22,),fg='black', bg='white',borderwidth=2,relief=SOLID)
mailentry.place(x=215, y=70)

passLabel = Label(frame, text='Password', font=('goudy old style', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=220, y=120)
pwd=StringVar()
passentry = Entry(frame, font=('arial', 22,),fg='black', bg='white',borderwidth=2,relief=SOLID,show='*')
passentry.place(x=215, y=160)
regbutton = Button(frame, text='Register New Account?', font=('arial', 11,'bold'), bd=0, fg='gray20', bg='white',
                   cursor='hand2', command=register_window,
                   activebackground='white', activeforeground='gray20')
regbutton.place(x=215, y=200)

forgetbutton = Button(frame, text='Forget Password?', font=('arial', 11,'bold'), bd=0, fg='red', bg='white',
                      cursor='hand2', command=forget_password,
                      activebackground='white', activeforeground='gray20')
forgetbutton.place(x=398, y=200)

loginbutton2 = Button(frame, text='Login', font=('eras medium itc', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=450, y=250)

backbutton1 = Button(frame, text='Back', font=('eras medium itc', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=back_command)
backbutton1.place(x=25, y=250)

root.maxsize(900,600)
root.minsize(900,600)
root.mainloop()
