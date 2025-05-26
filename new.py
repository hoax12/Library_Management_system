from tkinter import *
from tkinter import messagebox

import pymysql

root = Tk()
root.geometry("600x500")
frame1=Frame(root,width=600,height=80,borderwidth=5,relief=SOLID,bg='white')
frame1.place(x=0,y=0)
nameLabel = Label(frame1, text='UPDATE AND CHANGE RECORD USING GUI', font=('Kristen itc', 16, 'bold'), fg='black',
                                        bg='gray98')
nameLabel.place(x=10, y=10)

Label2=Label(root,text='Value',font=('Times New Roman',20,'bold'),bg='white',fg='black')
Label2.place(x=30,y=140)
value=StringVar()
entry1=Entry(root,bd=15,borderwidth=2,relief=SOLID,textvariable=value,width=30,font=('Times New Roman',15,'bold'))
entry1.place(x=120,y=145)

c=value.get()
print(c)

def insert():
    a=value.get()
    labelnew=Label(root,text='Inserted Value:' +a,font=('Times New Roman',18,'bold'))
    labelnew.place(x=150,y=300)
    entry1.delete(0,END)


def update():
    c = value.get()
    print(c)
    lqbel1=Label(root,text='Updated Value :'+c,font=('Times New Roman',18,'bold'))
    lqbel1.place(x=150,y=300)
    entry1.delete(0,END)


button1=Button(root,text='INSERT',borderwidth=2,relief=SOLID,font=('Times New Roman',15,'bold'),command=insert)
button1.place(x=120,y=200)

button2=Button(root,text='UPDATE',borderwidth=2,relief=SOLID,font=('Times New Roman',15,'bold'),command=update)
button2.place(x=230,y=200)

Label2=Label(root,text='By - Khot Mohammed Siddique',font=('Times New Roman',20,'bold'),bg='white',fg='black')
Label2.place(x=30,y=440)

def close():
    root.destroy()

button1=Button(root,text='CLOSE',borderwidth=2,relief=SOLID,font=('Times New Roman',15,'bold'),command=close)
button1.place(x=340,y=200)



root.mainloop()
