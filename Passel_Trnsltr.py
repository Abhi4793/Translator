# -*- coding: utf-8 -*-
"""
This is part of the ongoing development of Translator UI developed for the purpose of Hackademy2020.
"""

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as tkMessageBox

window = Tk()

label_frame = LabelFrame(window, borderwidth=2, width = 10, relief="ridge")
label_frame.pack(expand='yes', fill='both')

var = StringVar()
var.set("English(Default)")
data=( "English","German","French","Spanish","Chinese")
cb=Combobox(window, width = 22, height = 50, values=data)
cb.place(x=400,y=35)

label1 = Label(window, borderwidth = 2, width = 10, height = 2, relief="ridge", text="Langguage..")
label1.place(x=300, y=30)


def openNewWindow():
        
    newwindwow = Toplevel(window)
    newWindow.title("Configuration")
    newWindow.geometry("300x150")
    newWindowmaxsize(400, 180)

    label2 = Label(newWindow, text = "Glssary File Location..")
    label2.place(x=35, y=75) 
    
    btn_inner(newWindow, text="Browse", borderwidth = 2, width = 5, height = 2, relief="ridge", side=RIGHT, command=openNewWindow())
    btn_inner.place(x=35, y=25) 


def VideoBrowse():
    window.destinationdirectory = filedialog.askdirectory(initialdir = "C:\\Users\\Abhishek\\Resources")
    window.destinationText.insert('1', window.files_list)
    message.showinfo("Translation In Progress")


def DocumentBrowse():
    window.files_list = list(filedialog.askopenfilenames(initialdir = "C:\\Users\\Abhishek\\Resources"))
    window.sourceText.insert('1', window.files_list)
    message.showinfo("Translation In Progress")


btn = Button(label_frame, text ="Settings", borderwidth=2, width=28, height=2, relief="ridge", command = openNewWindow)
btn.place(x=35, y=25)

btn1 = Button(label_frame, text ="Call Trans", borderwidth=1, width=12, height=5, relief="ridge")
btn1.place(x=35, y=25)

btn2 = Button(label_frame, text ="Chat Trans", borderwidth=1, width=12, height=5, relief="ridge")
btn2.place(x=35, y=25)

btn3 = Button(label_frame, text ="Video Trans", borderwidth=1, width=12, height=5, relief="ridge", command = VideoBrowse())
btn3.place(x=35, y=25)

btn4 = Button(label_frame, text ="Document Trans", borderwidth=1, width=12, height=5, relief="ridge", command = DocumentBrowse())
btn4.place(x=35, y=25)

btn5 = Button(label_frame, text ="Text Trans", borderwidth=1, width=12, height=5, relief="ridge")
btn5.place(x=35, y=25)


window.title('Passel Translator')
window.geometry("600X200")
window.maxsize(600, 200)
window.mainloop()