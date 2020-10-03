
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as tkMessageBox
# from PIL import Image
# from PIL import ImageTk

window = Tk()

label_frame = LabelFrame(window, borderwidth=2, width = 10, relief="ridge")
label_frame.pack(expand='yes', fill='both')


var = StringVar()
var.set("English(Default)")
data=( "English","German","French","Spanish","Chinese")
cb=Combobox(window, width=22, height=50, values=data)
cb.place(x=400,y=35)

label1 = Label(window, borderwidth = 2, width = 10, height = 2, relief="ridge", text="Langguage..")
label1.place(x=300, y=30)

def Destinationfolder():
    Directory = filedialog.askdirectory(initialdir = "C:\\Users\\Public")
    
    window.OriginText.insert( '1', Directory)


def openNewWindow():
        
    newWindow = Toplevel(window)
    newWindow.title("Configuration")
    newWindow.geometry("300x200")
    newWindow.maxsize(300, 200)

    label2 = Label(newWindow, text = "Translated Resources Default Path..")
    label2.place(x=15, y=45) 
    
    browsebtn = Button(newWindow, text ="Browse", borderwidth=1, width=11, height=2, relief="ridge", command = Destinationfolder)
    browsebtn.place(x=210, y=37)
    
    # c1 = Tk.Checkbutton(newWindow, text='Disability Mode')
    # c1.place(x=15, y=145)

# icon1 = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Settings_icon.png")
# Callicon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Callicon.png")
# Chaticon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Chaticon.png")
# Docicon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Docicon.png")
# Videoicon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Videoicon.png")
# Texticon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Texticon.png")


btn = Button(label_frame, text ="Settings", borderwidth=2, width=28, height=2, relief="ridge", command = openNewWindow)
btn.place(x=35, y=25)

def ConsentWindow():
        
    CallWindow = Toplevel(window)
    CallWindow.title("Consent")
    CallWindow.geometry("375x100")
    CallWindow.maxsize(375, 100)

    label2 = Label(CallWindow, text = "This Call will be recorded for further Translation purposes.")
    label2.place(x=15, y=25) 
    
    Continuebutton = Button(CallWindow, text ="Continue", borderwidth=1, width=11, height=1, relief="ridge")
    Continuebutton.place(x=170, y=67)
    
    Declinebutton = Button(CallWindow, text ="Decline", borderwidth=1, width=11, height=1, relief="ridge")
    Declinebutton.place(x=280, y=67)

btn1 = Button(label_frame, text ="Call Translator", borderwidth=1, width=13, height=5, relief="ridge", command = ConsentWindow)
btn1.place(x=22, y=100)

#Function to open Chat application & active window selection
def openchatselection():
    
    ChatWindow = Toplevel(window)
    ChatWindow.title("Chat Selection")
    ChatWindow.geometry("300x150")
    ChatWindow.maxsize(300, 150)

    Applabel = Label(ChatWindow, text = "Select Application")
    Applabel.place(x=25, y=35)

#Chat application list
    var = StringVar()
    data=("Sametime", "Jabber")
    cb1=Combobox(ChatWindow, width=20, height=50, values=data)
    cb1.place(x=135, y=35)
 
    Activelabel = Label(ChatWindow, text = "Select Application")
    Activelabel.place(x=135, y=75)
#This section needs to be dynamic to get active windows from background
    var = StringVar()
    data=("Active Window 1", "Active Window 2")
    cb1=Combobox(ChatWindow, width=20, height=50, values=data)
    cb1.place(x=25, y=75)

btn2 = Button(label_frame, text ="Chat Translator", borderwidth=1, width=13, height=5, relief="ridge", command = openchatselection)
btn2.place(x=140, y=100)

def VideoBrowse():
    
    window.files_list = list(filedialog.askopenfilenames(initialdir = "C:\\Users\\Public\\Desktp"))
    
    window.SourceText.insert( '1', window.files_list)
    
    messagebox.showinfo("Translation in Progress")

btn3 = Button(label_frame, text ="Video Translator", borderwidth=1, width=13, height=5, relief="ridge", command = VideoBrowse)
btn3.place(x=255, y=100)

def DocumentBrowse():
    OriginDirectory = filedialog.askdirectory(initialdir = "C:\\Users\\Public\\Desktp")
    
    window.OriginText.insert( '1', OriginDirectory)
    
    messagebox.showinfo("Translation in Progress")
    
btn4 = Button(label_frame, text ="File Translator", borderwidth=1, width=13, height=5, relief="ridge", command = DocumentBrowse)
btn4.place(x=370, y=100)

btn5 = Button(label_frame, text ="Text Translator", borderwidth=1, width=13, height=5, relief="ridge")
btn5.place(x=485, y=100)


window.title("meetTranslate")
window.maxsize(610, 200)
window.geometry("610x200")
window.mainloop()