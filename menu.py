
from tkinter import*
m=Tk()
m.geometry("200x250")
menubutton= Menubutton(m,text="Language" ,relief= SOLID)
menubutton.grid()
menubutton.menu=Menu(menubutton)
menubutton["menu"]= menubutton.menu
menubutton.menu.add_checkbutton(label="Hindi",variable=IntVar())
menubutton.menu.add_checkbutton(label="English",variable=IntVar())
menubutton.pack()
m.mainloop()
