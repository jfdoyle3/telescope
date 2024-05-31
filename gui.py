from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Dalek")
frm=ttk.Frame(root,padding=10).grid()


lbl=Label(root, text="You shall be exterminated!!").grid(column=1, row=0)


def clicked():
    lbl.configure(text="I just got clicked") 
    lbl.grid(column=0,row=2)
    
btn=Button(root,text="Click me", fg="red", command=clicked)
btn.grid(column=0, row=1)

root.mainloop()