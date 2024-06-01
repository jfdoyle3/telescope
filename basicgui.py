from tkinter import *
from tkinter import ttk
frame = Tk()
frame.title("Lens Calculator")
frame.geometry('400x200')
frm = ttk.Frame(frame, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=frame.destroy).grid(column=1, row=5)
frame.mainloop()