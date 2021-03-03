from tkinter import*
c=Tk()

name=Label(c,text="Name").grid(row=0,column=0)
e1=Entry(c).grid(row=0,column=1)
firstname=Label(c,text="FirstName").grid(row=0,column=2)
e2=Entry(c).grid(row=0,column=3)
lastname=Label(c,text="LastName").grid(row=0,column=4)
e3=Entry(c).grid(row=0,column=5)
password=Label(c,text="password").grid(row=1,column=0)
e4=Entry(c).grid(row=1,column=1)
email=Label(c,text="Email").grid(row=2,column=0)
e5=Entry(c).grid(row=2,column=1)
DOB=Label(c,text="DOB").grid(row=3,column=0)
e6=Entry(c).grid(row=3,column=1)
c.geometry(200*200)
spin=Spinbox(c,from_1,to=31)
Date=spin.pack()
c.mainloop()

#expandable
