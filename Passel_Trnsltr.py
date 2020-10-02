
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as tkMessageBox
from PIL import Image
from PIL import ImageTk

window = Tk()

label_frame = LabelFrame(window, borderwidth=2, width = 10, bg= 'lightgrey", relief="ridge")
label_frame.pack(expand='yes', fill='both')


var = StringVar()
var.set("English(Default)")
data=( "English","German","French","Spanish","Chinese")
cb=Combobox(window, width=22, height=50, values=data)
cb.place(x=400,y=35)

label1 = Label(window, borderwidth = 2, width = 10, height = 2, relief="ridge", text="Langguage..")
label1.place(x=300, y=30)


def openwoindow():
        
    Settingswindwow = Toplevel(window)
    SettingsWindow.title("Configuration")
    SettingsWindow.geometry("300x150")
    SettingsWindow.maxsize(400, 180)

    label2 = Label(Settingswindow, text = "Path to the Application Log"")
    label2.place(x=35, y=25)

icon1 = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Settings_icon.png")
Callicon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Callicon.png")
Chaticon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Chaticon.png")
Docicon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Docicon.png")
Videoicon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Videoicon.png")
Texticon = PhotoImage(file = "C:\\Users\\Abhi\\Desktop\\Icons\\Texticon.png")


btn = Button(window, image=icon1, borderwidth=2, height=45, width=200, relief="ridge", compound = LEFT, command=openNewWindow)
btn.place=(x=35, y=25)

btn1 = Button(window, text = Call Translator, image=Callicon, borderwidth=1, height=90, width=100, relief="ridge")
btn1.place=(x=22, y=100)

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

btn2 = Button(window, text = Chat Translator, image=Chaticon, borderwidth=1, height=90, width=100, relief="ridge", command = openchatselection)
btn2.place=(x=140, y=100)

def VideoBrowse():
    
    window.files_list = list(filedialog.askopenfilenames(initialdir = "C:\\Users\\Abhi\\Desktp\\Resources"))
    
    window.SourceText.insert( '1', window.files_list)
    
    messagebox.showinfo("Translation in Progress")

btn3 = Button(window, text = Video Translator, image=Videoicon, borderwidth=1, height=90, width=100, relief="ridge", command = VideoBrowse)
btn3.place=(x=255, y=100)

def DocumentBrowse():
    OriginDirectory = filedialog.askdirectory(initialdir = "C:\\Users\\Abhi\\Desktp\\Resources")
    
    window.OriginText.insert( '1', OriginDirectory)
    
    messagebox.showinfo("Translation in Progress")
    
btn4 = Button(window, text = Document Translator, image=Docicon, borderwidth=1, height=90, width=100, relief="ridge", command = DocumentBrowse)
btn4.place=(x=370, y=100)

btn5 = Button(window, text = Text Translator, image=Texticon, borderwidth=1, height=90, width=100, relief="ridge")
btn5.place=(x=370, y=100)


window.title("Passel Translator")
window.maxsize(650, 200)
window.mainloop()
