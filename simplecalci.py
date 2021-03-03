from tkinter import*
m=Tk()
m.title("calculator")
m.resizable(0,0)
m.wm_attributes("-topmost", 1)
Label1=Label(m,text="CALCI")
Label1.grid(row=0, columnspan=8)

equa=""
equation =StringVar()
calculation=Label(m, textvariable=equation)
equation.set("Enter your expression")
calculation.grid(row=2,columnspan=8)

def btnPress(num):
    global equa
    equa = equa+str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total=str(eval(equa))
    equation.set(total)
    equa=""

def ClearPress():
    global equa
    equa=""
    equation.set("")


zero=Button(m,text="0", command=lambda:btnPress(0) , borderwidth=1, relief=SOLID)
zero.grid(row=6, column=2, padx=10, pady=10)
one=Button(m,text="1", command=lambda:btnPress(1) , borderwidth=1, relief=SOLID)
one.grid(row=3, column=1, padx=10, pady=10)
two=Button(m,text="2", command=lambda:btnPress(2) , borderwidth=1, relief=SOLID)
two.grid(row=3, column=2, padx=10, pady=10)
three=Button(m,text="3", command=lambda:btnPress(3) , borderwidth=1, relief=SOLID)
three.grid(row=3, column=3, padx=10, pady=10)
four=Button(m,text="4", command=lambda:btnPress(4) , borderwidth=1, relief=SOLID)
four.grid(row=4, column=1, padx=10, pady=10)
five=Button(m,text="5", command=lambda:btnPress(5) , borderwidth=1, relief=SOLID)
five.grid(row=4, column=2, padx=10, pady=10)
six=Button(m,text="6", command=lambda:btnPress(6) , borderwidth=1, relief=SOLID)
six.grid(row=4, column=3, padx=10, pady=10)
seven=Button(m,text="7", command=lambda:btnPress(7) , borderwidth=1, relief=SOLID)
seven.grid(row=5, column=1, padx=10, pady=10)
eight=Button(m,text="8", command=lambda:btnPress(8) , borderwidth=1, relief=SOLID)
eight.grid(row=5, column=2, padx=10, pady=10)
nine=Button(m,text="9", command=lambda:btnPress(9) , borderwidth=1, relief=SOLID)
nine.grid(row=5, column=3, padx=10, pady=10)
plus=Button(m,text="+", command=lambda:btnPress("+") , borderwidth=1, relief=SOLID)
plus.grid(row=6, column=5, padx=10, pady=10)
minus=Button(m,text="-", command=lambda:btnPress("-") , borderwidth=1, relief=SOLID)
minus.grid(row=5, column=5, padx=10, pady=10)
mul=Button(m,text="*", command=lambda:btnPress("*") , borderwidth=1, relief=SOLID)
mul.grid(row=5, column=4, padx=10, pady=10)
div=Button(m,text="/", command=lambda:btnPress("/") , borderwidth=1, relief=SOLID)
div.grid(row=6, column=1, padx=10, pady=10)
mod=Button(m,text="%", command=lambda:btnPress("%") , borderwidth=1, relief=SOLID)
mod.grid(row=6, column=3, padx=10, pady=10)
sq=Button(m,text="sq", command=lambda:btnPress("sq") , borderwidth=1, relief=SOLID)
sq.grid(row=6, column=4, padx=10, pady=10)
Equal=Button(m,text="=", command=EqualPress , borderwidth=1, relief=SOLID)
Equal.grid(row=4, column=4, padx=10, pady=10)
clear=Button(m,text="CE", command=ClearPress, borderwidth=1, relief=SOLID)
clear.grid(row=3, column=4, padx=10, pady=10)
cross=Button(m,text="x", command=ClearPress, borderwidth=1, relief=SOLID)
cross.grid(row=3, column=5, padx=10, pady=10)
rat=Button(m,text="0", command=lambda:btnPress(0) , borderwidth=1, relief=SOLID)
rat.grid(row=4, column=5, padx=10, pady=10)


m.mainloop()
