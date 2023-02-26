import mysql.connector
from tkinter import messagebox
from tkinter import *

#database name : python
#table name : mydatabase

db = mysql.connector.connect(host="localhost",user="root",password="",database="python")
def insert():
    c=db.cursor()
    i=e.get()
    p=e1.get()
    sql="""INSERT INTO mydatabase values(%s,%s)"""
    c.execute(sql,(i,p))
    db.commit()
    messagebox.showinfo("Congrats","SignUp successful")
    db.close()
def retrieve():
    c=db.cursor()
    i=e.get()
    p=e1.get()
    sql="""SELECT * FROM mydatabase"""
    c.execute(sql)
    result=c.fetchall()
    for row in result:
        if i in row[0]:
            if p in row[1]:
                messagebox.showinfo("Congrats","Login Successful")           
            else:
                messagebox.showinfo("Alert","Login failed")


win=Tk()
        
l=Label(win,text="UserName").grid(row=0,column=0)
e=Entry(win)
e.grid(row=0,column=1)

l1=Label(win,text="Password").grid(row=1,column=0)
e1=Entry(win,show="*")
e1.grid(row=1,column=1)
b=Button(win,text="SignUp",command=insert).grid(row=2,column=0)
b=Button(win,text="Login",command=retrieve).grid(row=2,column=1)

    
win.mainloop()
