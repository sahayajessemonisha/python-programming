from tkinter import *
import sqlite3
from tkinter import messagebox

r=Tk()
r.geometry('500x500')
r.title('Registration Form')
r.config(bg='pink')

Fullname=StringVar()
Email=StringVar()
var=IntVar()
c=StringVar()
var1=IntVar()
var2=IntVar()



def db():
    name=Fullname.get()
    email=Email.get()
    gender=var.get()
    country=c.get()
    pro=var1.get()
    conn=sqlite3.connect('Alen.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Students(Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        cursor.execute('INSERT INTO Students(Fullname,Email,Gender,country,Programming)Values(?,?,?,?,?)',(name,email,gender,country,pro))
        conn.commit()
        messagebox.showinfo('Information','Table created successfully')
        
        print("Table created")
l1=Label(r,text='REGISTRATION FORM',font=('Arial',15,'bold'),bg='black',fg='pink',)
l1.place(x=125,y=53)
l2=Label(r,text="FULL NAME",font=('Arial',12,'bold'),bg='pink')
l2.place(x=80,y=130)
e1=Entry(r,textvar=Fullname,font=('arial',12),fg='orange')
e1.place(x=245,y=130)
l2=Label(r,text="EMAIL",font=("Arial",12,'bold'),bg='pink')
l2.place(x=80,y=180)
e2=Entry(r,textvar=Email,font=('Arial',12))
e2.place(x=245,y=180)
l3=Label(r,text="GENDER",font=("Arial",12,'bold'),bg='pink')


l3.place(x=80,y=230)
Radiobutton(r,text="Male",variable=var,value=1,font=('Arial',12),fg='blue').place(x=245,y=230)
Radiobutton(r,text="Female",variable=var,value=2,font=('Arial',12),fg='red').place(x=315,y=230)
l4=Label(r,text='COUNTRY',font=('Arial',12,'bold'),bg='pink')
l4.place(x=80,y=280)
list1=['Australia','India','Pakistan','South Africa','Afganistan','England']
droplist=OptionMenu(r,c,*list1)
droplist.config(width=15)
c.set('Select your country')
droplist.place(x=245,y=280)
l5=Label(r,text="PROGRAMMING",font=('Arial',12,'bold'),bg='pink')
l5.place(x=80,y=330)
Checkbutton(r,text='Java',font=('Arial',12),fg='green',variable=var1).place(x=245,y=330)
Checkbutton(r,text='Python',font=('Arial',12),fg='indigo',variable=var2).place(x=312,y=330)

Button(r,text='Submit',font=('Arial',13,'bold'),bg='blue',fg='white',command=db).place(x=190,y=400)
r.mainloop()
