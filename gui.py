from tkinter import *

root=Tk()
root.title("Dalek")
root.geometry('350x200')


lbl =Label(root, text="You shall be exterminated!!")
lbl.grid()

def clicked():
    lbl.configure(text="I just got clicked")
    
btn=Button(root,text="Click me", fg="red", command=clicked)
btn.grid(column=1, row=0)


# Quit program
Button(root,text="quit", command=quit).grid(column=2,row=0, sticky=W)

def quit():
    root.destroy()
    exit()
    
    
root.mainloop()