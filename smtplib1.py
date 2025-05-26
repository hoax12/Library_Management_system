import smtplib
from email.message import EmailMessage
from datetime import timedelta,date

import pymysql

msg=EmailMessage()
con =pymysql.connect(host='localhost', user='root', password='Sid@1234', database='myprojectdb')
cursor = con.cursor()
cursor.execute("SELECT email FROM employee1 WHERE user_id='20101A0053'",)
var = cursor.fetchone()
'''
cursor.execute("SELECT issue_date FROM book_issued WHERE book_id=2 and student_id='20101A0048'")
var1 = cursor.fetchone()'''

cursor.execute("SELECT name from books_info WHERE id=1",)
var1 = cursor.fetchone()

cursor.execute("SELECT f_name from employee1 WHERE user_id='20101A0053'")
var2 = cursor.fetchone()

str = ''.join(var)
str1 = ''.join(var1)
str2 = ''.join(var2)

#print(str1)
#print(str)
#print(str2)

issue_date = (date.today())
r=timedelta(days=90)
return_date = issue_date + r

#print(issue_date)
#print(return_date)
#print("Issue Date",issue_date,"\nReturn Date",return_date)
#print("Your book has been Issued from our library\nBook Name :",str1,"\nIssue Date :",issue_date,"\nReturn Date :",return_date,"\nThank you for Issuing the book from our library")
a="LIBRARY DEPARTMENT\nLibrary Issued Books Department Hello",str2," Your book has been Issued from our library\nBook Name :",str1,"\nIssue Date :",issue_date,"\nReturn Date :",return_date,"\nThank you for Issuing the book from our library"
msg['Subject']='Book issued from 24/7 Library'
msg['From']='24/7 Library'
msg["To"]=str
msg.set_content("""LIBRARY DEPARTMENT\nLibrary Issued Books Department\nHello Your book has been Issued from our library\nThank you for Issuing the book from our library""")
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('rajneeshpaul12@gmail.com','rajneesh@12')
server.send_message(msg)
server.quit()

print("Message Sent succesfully")