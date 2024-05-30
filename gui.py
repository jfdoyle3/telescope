from tkinter import *

root=Tk()
root.title("Lens Calculcator")
root.geometry('350x200')


def click():
    enteredText=textEntry.get()
    print(enterText)


# Label - Text
lblMagnification =Label(root, text="Enter lens magnification").grid(row=0,column=0)

#Text Box
textEntry=Entry(root,width=20,bg="white").grid(row=2,column=0, sticky=W)

#Submit button
Button(root,text="SUBMIT",width=6,command=click).grid(row=3,column=0, sticky=W)

#OutputBox
output=Text(root,width=75,height=6,wrap=WORD,background="white").grid(row=5,column=0,columnspan=2, sticky=W)


"""    
btn=Button(root,text="Click me", fg="red", command=clicked)
btn.grid(column=1, row=0)



def clicked():
    lbl.configure(text="I just got clicked")
"""   
# Quit program
Button(root,text="quit", command=quit).grid(row=0,column=50, sticky=W)

def quit():
    root.destroy()
    exit()
    
  
    
root.mainloop()