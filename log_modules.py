from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
def userlogin_window():
    root.destroy()
    import user_login
def admLogin_window():
    root.destroy()
    import login

root = Tk()
root.geometry('900x600+50+50')
root.title('Library Management System')
bglogin = PhotoImage(file='bgpic.png')
bgloginLabel = Label(root, image=bglogin)
bgloginLabel.place(x=0, y=0)
frame = Frame(root, bg='gray98', width=600, height=450,borderwidth=8,relief=SOLID)
frame.place(x=150, y=70)

'''forgetLabel = Label(root, text='THE  24/7', font=('Mistral', 32, 'bold'), fg='black', bg='white')
forgetLabel.place(x=228, y=98)'''
forgetpassLabel = Label(root, text='THE  24/7 LIBRARY...', font=('Kristen itc', 33, 'bold'), fg='black',
                                        bg='gray98')
forgetpassLabel.place(x=205, y=105)

userimage = PhotoImage(file='adminpic.png')
userimageLabel = Label(root, image=userimage, bg='white',borderwidth=3,relief=SOLID)
userimageLabel.place(x=215, y=200)
userimage1 = PhotoImage(file='picuser.png')
userimageLabel1 = Label(root, image=userimage1, bg='white',borderwidth=3,relief=SOLID)
userimageLabel1.place(x=485, y=200)
loginbutton2 = Button(root,width= 13, text='User Login', font=('eras medium itc', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      background='gray30', foreground='white',command=userlogin_window,borderwidth=5,relief=SOLID)
loginbutton2.place(x=485, y=425)
loginbutton1 = Button(root,width= 13, text='Admin Login', font=('eras medium itc', 18, 'bold'), fg='white', bg='black', cursor='hand2',
                      background='gray30', foreground='white',command=admLogin_window,borderwidth=5,relief=SOLID)
loginbutton1.place(x=215, y=425)

root.maxsize(900,600)
root.minsize(900,600)
root.focus_force()
root.grab_set()
root.mainloop()