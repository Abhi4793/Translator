from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as tkMessageBox
from PIL import Image
from PIL import ImageTk
from googletrans import Translator
import os
import pandas as pd
import numpy as np
import PyPDF2
from pydub.silence import split_on_silence
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS



translator = Translator()
window = Tk()

label_frame = LabelFrame(window,borderwidth=2, relief="ridge")
label_frame.pack(expand='yes', fill='both')


var = StringVar()
var.set("English(Default)")
data=( "English(Default)","German","French","Spanish","Chinese")
cb=Combobox(window, width=22, height=55, values=data)
cb.place(x=400,y=40)

label1 = Label(window, text="Language..", borderwidth = 2, width = 10, height = 2 )
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

Settings = PhotoImage(file = "Settings.png")
Callicon = PhotoImage(file = "Callicon.png")
Chaticon = PhotoImage(file = "Chaticon.png")
Docicon = PhotoImage(file = "Docicon.png")
Videoicon = PhotoImage(file = "Video_icon.png")
Texticon = PhotoImage(file = "Texticon.png")
Muteicon = PhotoImage(file="Muteicon.png")
Volumeicon = PhotoImage(file="Volumeicon.png")

btn = Button(label_frame, image = Settings, borderwidth=2, width=200, height=42, relief="ridge", command = openNewWindow)
btn.place(x=20, y=25)


def openCallWindow():
       
    CallWindow = Toplevel(window)
    CallWindow.title("Ongoing Call")
    CallWindow.geometry("300x200")
    CallWindow.maxsize(300, 200)
   
    def Mutemic():
        Volumebtn.configure(image=Muteicon)
   
    Volumebtn = Button(CallWindow, image = Volumeicon, borderwidth=1, width=30, height=30, relief="ridge", command = Mutemic)
    Volumebtn.place(x=125, y=110)
   

def ConsentWindow():
       
    ConsentWindow = Toplevel(window)
    ConsentWindow.title("Consent")
    ConsentWindow.geometry("375x100")
    ConsentWindow.maxsize(375, 100)
       
    label2 = Label(ConsentWindow, text = "This Call will be recorded for further Translation purposes.")
    label2.place(x=15, y=25)

    Continuebutton = Button(ConsentWindow, text ="Continue", borderwidth=1, width=11, height=1, relief="ridge", command = openCallWindow)
    Continuebutton.place(x=170, y=67)
   
    Declinebutton = Button(ConsentWindow, text ="Decline", borderwidth=1, width=11, height=1, relief="ridge", command = ConsentWindow.destroy)
    Declinebutton.place(x=280, y=67)
   
   
btn1 = Button(label_frame, image = Callicon, text ="Call Translator", borderwidth=1, width=100, height=95, relief="ridge", command = ConsentWindow)
btn1.place(x=20, y=85)

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
    Activelabel.place(x=25, y=75)
#This section needs to be dynamic to get active windows from background
    var = StringVar()
    data=("Active Window 1", "Active Window 2")
    cb1=Combobox(ChatWindow, width=20, height=50, values=data)
    cb1.place(x=135, y=75)

btn2 = Button(label_frame, image = Chaticon, text ="Chat Translator", borderwidth=1, width=100, height=95, relief="ridge", command = openchatselection)
btn2.place(x=140, y=85)

def VideoBrowse():

    filename = filedialog.askopenfilename(initialdir = "C:\\Users\\Abhishek\\Desktop\\aToV")
   
    clip = mp.VideoFileClip(filename)
    clip.audio.write_audiofile(r"Test_audio.wav")
   
    r = sr.Recognizer()
   
    # a function that splits the audio file into chunks
    # and applies speech recognition
    def get_large_audio_transcription(path):
        """
        Splitting the large audio file into chunks
        and apply speech recognition on each of these chunks
        """
        # open the audio file using pydub
        sound = AudioSegment.from_wav(path)  
        # split audio sound where silence is 700 miliseconds or more and get chunks
        chunks = split_on_silence(sound,
            # experiment with this value for your target audio file
            min_silence_len = 500,
            # adjust this per requirement
            silence_thresh = sound.dBFS-14,
            # keep the silence for 1 second, adjustable as well
            keep_silence=500,
        )
        folder_name = "audio-chunks"
        # create a directory to store the audio chunks
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        # process each chunk
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                # try converting it to text
                try:
                   
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error: Could be music", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    print(chunk_filename, ":", text)
                    whole_text += text
        # return the text for all chunks detected
        return whole_text
   
   
    def doc_trans():
        f = open('text.txt', 'r')
        contents = f.read()
        print(contents)
        file_translate = Translator()
        result = file_translate.translate(contents, dest='fr')
        print(result.text)
        with open('textTranslated.txt', 'w',encoding="utf-8") as f:
            f.write(result.text)
   
   
    def combine_audio(vidname, audname, outname, fps=25):
        import moviepy.editor as mpe
        my_clip = mpe.VideoFileClip(vidname)
        audio_background = mpe.AudioFileClip(audname)
        final_clip = my_clip.set_audio(audio_background)
        final_clip.write_videofile(outname,fps)
        os.system(outname)
   
    def textToSpeech(filename):
        file = open(filename, "r",encoding="utf-8").read().replace("\n", " ")
        language = 'fr'
        speech = gTTS(text = str(file), lang = language, slow = False)
        speech.save("voice.mp3")
        #os.system("start voice.mp3")
   
    path = "Test_audio.wav"
    full_Text=get_large_audio_transcription(path)
    with open("text.txt","w+") as file:
        file.writelines(full_Text)
    doc_trans()
    textToSpeech("textTranslated.txt")
    combine_audio("HBFR_Mandatory_Compliance_Training.mp4","voice.mp3","HBFR_Mandatory_Compliance_Training_FR.mp4")
    messagebox.showinfo("Showinfo","File Saved")
    # window.OriginDirectory = list(filedialog.askopenfilenames(initialdir = "C:\\Users\\Riyaz\\Desktop"))
   
    # window.SourceText.insert( '1', window.OriginDirectory)
   
    # messagebox.showinfo("Translation in Progress")
       
    #messagebox.showinfo("Translation in Progress")

btn3 = Button(label_frame, image = Videoicon, text ="Video Translator", borderwidth=1, width=100, height=95, relief="ridge", command = VideoBrowse)
btn3.place(x=255, y=85)


def DocumentBrowse():
    filename = filedialog.askopenfilename(initialdir = "C:\\Users\\Abhishek\\Desktop")
    if os.path.splitext(filename)[1] == ".txt" :
        file1 = open(filename,"r")
        text_to_translate = file1.read()
        file1.close()
        text_translated = translator.translate(text_to_translate, dest = 'fr')

        file2 = open(os.path.splitext(filename)[0]+"_translated.txt","w")
        file2.write(text_translated.text)
        file2.close()

    if os.path.splitext(filename)[1] == ".csv" :
        df = pd.read_csv (filename)
        cols_new = []
        def translate(x):
            text_to_translate = str(x)
            text_translated = translator.translate(text_to_translate, dest = 'fr')
            return text_translated.text

        for cols in np.array(df.columns):
            df[cols] = df[cols].apply(translate)
       
        for i in range(df.shape[1]):
            cols_new.append(translate(df.columns[i]))
        df.columns = cols_new

        df.to_csv(os.path.splitext(filename)[0]+"_translated.csv", index=False)

    if os.path.splitext(filename)[1] == ".pdf" :
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        file2 = open(os.path.splitext(filename)[0]+"_translated.txt","w")
       
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            text = pageObj.extractText()
            text = text.replace('e.g.', 'e#g#')
            if(text.find('http') >= 0):
                text = text.replace(text[text.find('http'):text.find(' ',text.find('http'))],text[text.find('http'):text.find(' ',text.find('http'))].replace('\n','').replace('.','#'))
            texts = text.split('.')
            for t in texts:
                text_to_translate = t.replace('\n','').replace('#','.').replace('  ','\n').strip() + '.'
                text_translated = translator.translate(text_to_translate, dest = 'fr')
                file2.write(text_translated.text)
            file2.write("\n---------------END OF PAGE--------------\n")
        file2.close()
    messagebox.showinfo("Showinfo","File Saved")
   
btn4 = Button(label_frame, image = Docicon, text ="File Translator", borderwidth=1, width=100, height=95, relief="ridge", command = DocumentBrowse)
btn4.place(x=370, y=85)

def TextTranslator():
    quickTextwindow = Toplevel(window)
    quickTextwindow.title("Quick Text Translator")
    quickTextwindow.maxsize(510, 225)
    quickTextwindow.geometry("510x225")
    
    #Creating a Frame and Grid to hold the Content
    mainframe = Frame(quickTextwindow, borderwidth=2, relief="ridge")
    mainframe.pack(expand='yes', fill='both')
    
    #variables for dropdown list
    lan1 = StringVar(quickTextwindow)
    lan2 = StringVar(quickTextwindow)
    
    #choices to show in dropdown menu
    choices = { 'English','French','Hindi','Gujarati','Spanish','German', 'Bengali' }
    #default selection for dropdownlists
    lan1.set('English')
    lan2.set('French')
    
    #creating dropdown and arranging in the grid
    lan1menu = OptionMenu( mainframe, lan1, *choices)
    lan1menu.place(x = 140, y = 40)
    Label1 = Label(mainframe,text="Source language")
    Label1.place( x = 20, y = 45 )
    
    
    lan2menu = OptionMenu( mainframe, lan2, *choices)
    Label2 = Label(mainframe,text="Target language")
    lan2menu.place(x= 410, y =40)
    Label2.place( x = 290, y = 45 )
    
    #Text Box to take user input
    Label(mainframe, text = "Enter text")
    var = StringVar()
    textbox = Entry(mainframe, textvariable=var)
    textbox.place( width=200, height=95, x= 20, y= 80)
    
    #textbox to show output
    #label can also be used
    Label(mainframe, text = "Output")
    var1 = StringVar()
    textbox = Entry(mainframe, textvariable=var1)
    textbox.place( width=200, height=95, x= 290, y= 80)

    #Translator function 
    def translate():
        translator= Translator()
        translation = translator.translate(var.get(), src = lan1.get(),dest = lan2.get())
        var1.set(translation.text)
    
    #creating a button to call Translator function
    b1=Button(mainframe,text='Translate',command=translate)
    b1.place(x = 226, y = 100)
    
    def ClearTextInput():
        var1.set('')
        var.set('')

    b2=Button(mainframe,text='Clear',width = 7, command=ClearTextInput)
    b2.place(x = 226, y = 150)


btn5 = Button(label_frame, image = Texticon, borderwidth=1, width=100, height=95, relief="ridge",command = TextTranslator)
btn5.place(x=485, y=85)


window.title("meetTranslate")
window.maxsize(610, 200)
window.geometry("610x200")
window.mainloop()
