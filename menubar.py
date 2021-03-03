from tkinter import*
top=Tk()
def hello():
    print("hello!")
def quit():
    print("i quit")

    
#create a top level menu
menubar=Menu(top)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=quit)
#display th menu
top.config(menu=menubar)
top.mainloop()
