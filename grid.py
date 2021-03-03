
from tkinter import*
parent=Tk()
name=Label(parent,text="Name").grid(row=1,column=1)
e1=Entry(parent).grid(row=1,column=2)
password=Label(parent,text="Password").grid(row=2,column=1)
e2=Entry(parent).grid(row=2,column=2)
submit=Button(parent,text="Submit").grid(row=4,column=1)
parent.mainloop()
