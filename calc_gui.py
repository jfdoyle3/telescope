import tkinter as tk
from objects.zhumell114 import *

telescope = Zhumell114()

# Top level window

frame = tk.Tk()

frame.title("Calculator")

frame.geometry("200x200")
# Function for getting Input
# from textbox and printing it
# at label widget


def printInput():

    inp = inputtxt.get(1.0, "end-1c")
    print(inp)
    lbl.config(
        text=telescope.name + " Base Telescope stats\n--------------------------------"
    )
    lbl.configure(text="Focal Length: " + str(telescope.focalLength) + "mm")


# TextBox Creation

lens = tk.Label(frame, text="Lens in mm")
lens.pack()
inputtxt = tk.Text(frame, height=1, width=20)


inputtxt.pack()


# Button Creation

printButton = tk.Button(frame, text="Caculate", command=printInput)
printButton.pack()


# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()

frame.mainloop()
