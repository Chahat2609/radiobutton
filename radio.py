from tkinter import*
def selection():
    selection="you selected the option"+str(radio.get())
    label.config(text=selection)
c=Tk()
c.geometry("300x150")
radio=IntVar()
lbl=Label(text="Favourite Programming Language:")
lbl.pack()
R1=Radiobutton(c,text="C", variable=radio, value=1, command=selection)
R1.pack(anchor=W)
R2=Radiobutton(c,text="C++", variable=radio, value=2, command=selection)
R2.pack(anchor=W)
R3=Radiobutton(c,text="JAVA", variable=radio, value=3, command=selection)
R3.pack(anchor=W)
R4=Radiobutton(c,text="PYTHON", variable=radio, value=3, command=selection)
R4.pack(anchor=W)
R5=Radiobutton(c,text="C#", variable=radio, value=3, command=selection)
R5.pack(anchor=W)
label=Label(c)
label.pack()
c.mainloop()

