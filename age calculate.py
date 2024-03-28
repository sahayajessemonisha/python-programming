from tkinter import*
import datetime

a=Tk()
a.title("Age Calculator Website")
name=Label(a,text="Name")
name.grid(row=1,column=0)
year=Label(a,text="Year")
year.grid(row=2,column=0)
month=Label(a,text="Month")
month.grid(row=3,column=0)
date=Label(a,text="Date")
date.grid(row=4,column=0)


e1=Entry(a)
e1.grid(row=1,column=1)
e2=Entry(a)
e2.grid(row=2,column=1)
e3=Entry(a)
e3.grid(row=3,column=1)
e4=Entry(a)
e4.grid(row=4,column=1)

def input():
    name=e1.get()
    x=Person(name,datetime.date(int(e2.get()),int(e3.get()),int(e4.get())))
    textArea=Text(master=a,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer="heyy {x}!!! You are {age} yeara old!!!".format(x=name,age=x.age())
    textArea.insert(END,answer)
button=Button(a,text="Calculate Age", command=input, bg="pink")
button.grid(row=5,column=1)

class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate
    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age
a.mainloop()
