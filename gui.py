import subprocess
import threading
import time
import tkinter
import customtkinter  # <- import the CustomTkinter module
from tkinter import filedialog, HORIZONTAL, DISABLED, NORMAL
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk  # <- import PIL for the images
import os
from datetime import datetime, date
import transcribe
import subprocess
import time

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"

#Replace <command=example> with <command=threading.Thread(target=example).start>

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
root_tk.geometry("1150x700")
root_tk.title("Realtime Meeting Summarizer")

global p9

global flag
flag=0
global recflag
recflag = 0
global wflag
wflag = 0

def setflagt():
    global flag
    flag=0
    #print(flag)

def setflag():
    global flag
    flag=1
    #print(flag)


def button_function():
    global recflag
    global wflag
    fileno = len(os.listdir('Transcripts'))
    newfno = fileno
    counter=0

    recflag = (recflag+1)%2
    if (recflag == 1):


        p2=subprocess.Popen(["python","writeflag.py"],shell=True)
        button_img = customtkinter.CTkButton(master=frame_1, corner_radius=170, image=mic_image, text="",
                                             fg_color="red", command=threading.Thread(target=button_function).start, width=250, height=250,
                                             border_color="red", border_width=2)
        button_img.pack(pady=300, padx=10)
        button_img.place(relx=0.10, rely=0.30)
        praudio = subprocess.Popen(["python", "Rec.py"], shell=True)
       # praudio.wait()
    else:
        p2 = subprocess.Popen(["python", "writeflag.py"], shell=True)
        p2.wait
        button_img = customtkinter.CTkButton(master=frame_1, corner_radius=170, image=mic_image, text="",
                                             fg_color="white", command=threading.Thread(target=button_function).start,
                                             width=250, height=250,
                                             border_color="white", border_width=2)
        button_img.pack(pady=300, padx=10)
        button_img.place(relx=0.10, rely=0.30)
        button_1.configure(state=DISABLED)
        button_img.configure(state=DISABLED)
        entry_1.configure(state=DISABLED)
        button_2.configure(state=DISABLED)
        iloadingwords = "Converting from speech to text...."

        while (newfno == fileno):
            counter = counter + 1;
            newfno = len(os.listdir('Transcripts'))
            time.sleep(1)
            loadingwords = iloadingwords[:31+(counter % 4)]
            status_label['text'] = loadingwords
        status_label['text'] = "Converted"
        button_1.configure(state=NORMAL)
        button_img.configure(state=NORMAL)
        entry_1.configure(state=NORMAL)
        button_2.configure(state=NORMAL)


def sumbutton():
    status_label['text'] = "Summarizing..."
    button_1.configure(state=DISABLED)
    button_img.configure(state=DISABLED)
    entry_1.configure(state=DISABLED)
    button_2.configure(state=DISABLED)
    p3 = subprocess.Popen(["python", "sp.py"], shell=True)
    p3.wait()
    button_1.configure(state=NORMAL)
    button_img.configure(state=NORMAL)
    entry_1.configure(state=NORMAL)
    button_2.configure(state=NORMAL)

    p4 = subprocess.Popen(["python", "gui2.py"], shell=True)
    #p4.wait()
    root_tk.destroy()

def openfunc():
    openop()
    if flag==1:
        t1 = threading.Thread(target=wloop)
        t1.start()


def wloop():
    print("test")
    global p9
    poll = p9.poll()
    print(poll)
    counter= 0
    while poll is None:
        poll = p9.poll()
        button_1.configure(state=DISABLED)
        button_img.configure(state=DISABLED)
        entry_1.configure(state=DISABLED)
        button_2.configure(state=DISABLED)
        time.sleep(1)
        iloadingwords= "Converting from audio to text...."
        loadingwords = iloadingwords[:30 + (counter % 4)]
        status_label['text'] = loadingwords
        counter = counter+1
    status_label['text'] = "Converted"
    button_1.configure(state=NORMAL)
    button_img.configure(state=NORMAL)
    entry_1.configure(state=NORMAL)
    button_2.configure(state=NORMAL)





def openop():
    # print(flag)
    if flag == 0:
        file = filedialog.askopenfilename(initialdir="", title="Select File",filetypes=(("Text file", ".txt"), ("All files", ".*")))
        entry_1.insert(0, file)
        print(file)

        f = open(file, "r")
        text=f.read()
        f.close()

        #text=" "

        with open('Transcripts/transcript.txt', 'w') as fi:
            fi.write(text)
        fi.close()



    else:
        file = filedialog.askopenfilename(initialdir="", title="Select File",filetypes=(("Audio file", ".wav"), ("All files", ".*")))
        entry_1.insert(0, file)

        global p9
        p9 = subprocess.Popen(["python", "transcribe.py", file, "--local", "--api_key", "964420e2607e4374b3fe3378113b4e5d"],shell=True)


y_padding = 13

frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=20, padx=30, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1,text="REALTIME MEETING SUMMARIZER",width=220,height=55,text_font=("Calibri",32),fg_color="Grey")
label_1.pack(pady=y_padding, padx=30)

status_label = customtkinter.CTkLabel(master=frame_1, text="", width=220, height=10,text_font=("Calibri", 16))
status_label.pack(pady=y_padding, padx=30)

#Right part
radiobutton_var = tkinter.IntVar(value=1)

label_2 = customtkinter.CTkLabel(master=frame_1,text="Upload File",width=220,height=55,text_font=("Times New Roman",20))
label_2.pack(pady=y_padding, padx=30)
label_2.place(relx=0.67,rely=0.20)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1,text="Text",command=setflagt)
radiobutton_1.pack(pady=15, padx=15)
radiobutton_1.place(relx=0.725,rely=0.35)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2,text="Audio",command=setflag)
radiobutton_2.pack(pady=y_padding, padx=10)
radiobutton_2.place(relx=0.725,rely=0.4)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Filepath...")
entry_1.pack(pady=y_padding, padx=10)
entry_1.place(relx=0.675,rely=0.50)

button_2 = customtkinter.CTkButton(master=frame_1, corner_radius=8,text="Upload File", command=openfunc,state=NORMAL)
button_2.pack(pady=y_padding, padx=30)
button_2.place(relx=0.79,rely=0.50)

#################

#Left part

label_3 = customtkinter.CTkLabel(master=frame_1,text="Start Meeting",width=220,height=55,text_font=("Times New Roman",20))
label_3.pack(pady=y_padding, padx=30)
label_3.place(relx=0.12,rely=0.20)

image_size=160
mic_image = ImageTk.PhotoImage(Image.open(r"guistuff/mic.png").resize((image_size, image_size)))

button_img = customtkinter.CTkButton(master=frame_1, corner_radius=8,image=mic_image,text="",fg_color="White", command=threading.Thread(target=button_function).start,width=250,height=250,text_font=("Sans",18))
button_img = customtkinter.CTkButton(master=frame_1, corner_radius=170,image=mic_image,text="",fg_color="White", command=button_function,width=250,height=250,border_color="White",border_width=2,state=NORMAL)
button_img.pack(pady=300, padx=10)
button_img.place(relx=0.10,rely=0.30)

#############
button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=8,text="Summarize", command=threading.Thread(target=sumbutton).start,width=150,height=45,text_font=("Sans",18),state=NORMAL)
button_1.pack(pady=300, padx=10)
button_1.place(relx=0.45,rely=0.8)

s_var = tkinter.StringVar(value="on")


root_tk.mainloop()