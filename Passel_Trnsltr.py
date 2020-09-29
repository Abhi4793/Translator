# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import messagebox as tkMessageBox


window = Tk()

label_frame = labelFrame(window, borderwidth=2, width = 10, relief="ridge")
label_frame.pack(expand='yes', fill='both')
s = Style()
s.configure('My.TFrame', background='lightgrey')

var = Stringvar()
var.set("English(Default)")
data=( "English","German","French","Spanish","Chinese")
cb=Combobox(window, width=22, height=50, values=data)
cb.place(x=400,y=35)

label1 = Label(window, borderwidth = 2, width = 10, height = 2, relief="ridge", text="Langguage..")
label1.place(x=300, y=30)


def openwoindow():
        
    newwindwow = Toplevel(window)
    newWindow.title("Configuration")
    newWindow.geometry("300x150")
    newWindowmaxsize(400, 180)

    label2 = Label



mail1 = Frame(window, style='My.TFrame')
mail1.place(height=70, width=400, x=10, y=10)
mail1.config()
window.mainloop()