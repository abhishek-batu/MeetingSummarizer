import subprocess
import threading
import time
import tkinter
import customtkinter  # <- import the CustomTkinter module
from tkinter import filedialog, HORIZONTAL, DISABLED, NORMAL
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk  # <- import PIL for the images
import os
from fpdf import FPDF
import datetime

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

open_file = open('Transcripts/summary.txt', 'r')
summary=open_file.read()
if len(summary)>1050:
    summary=summary[:1050]+"..."
open_file.close()


def backbutton():
    root_tk.destroy()
    p1 = subprocess.Popen(["python", "gui.py"], shell=True)
    #p1.wait()

def pdfclick():
    today = datetime.datetime.now()
    dateS = str(today.strftime("%c"))
    dateS = dateS[4:-5]
    #dateS = dateS.replace(":", "-")
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", "U", 20)

    pdf.cell(200, 10, txt="Meeting Summary",ln=1, align='C',)

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=dateS, ln=1, align='C', )
    pdf.cell(200, 10, txt="", ln=1, align='C', )
    # open the text file in read mode
    #pdf.set_font("Arial", size=15)
    f = open("Transcripts/summary.txt", "r")
    # insert the texts in pdf
    pdf.set_font("Arial", size=15)
    for x in f:
        pdf.multi_cell(185, 10, txt=x, align='C')
    # save the pdf with name .pdf
    pdf.output("Summary.pdf")
    os.startfile("Summary.pdf")


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Replace <command=example> with <command=threading.Thread(target=example).start>

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
root_tk.geometry("1150x700")
root_tk.title("Result")

y_padding = 13

frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=20, padx=30, fill="both", expand=True)


label_1 = customtkinter.CTkLabel(master=frame_1,text="SUMMARY",width=220,height=55,text_font=("Calibri",32),fg_color="Grey")
label_1.pack(pady=y_padding, padx=30)

label_2 = customtkinter.CTkLabel(master=frame_1, text=summary,width=800,height=400, wraplength=785, justify="center",text_font=("Arial",18))
label_2.pack(pady=y_padding, padx=10)
label_2.place(relx=0.5,rely=0.5,anchor="center")

button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=8,text="Save as PDF",width=150,height=45,text_font=("Sans",18),state=NORMAL,command=pdfclick)
button_1.pack(pady=300, padx=10)
button_1.place(relx=0.5,rely=0.95,anchor="center")

button_2 = customtkinter.CTkButton(master=frame_1, corner_radius=8,text="Back",text_font=("Sans",14),state=NORMAL,command=backbutton)
button_2.pack(pady=300, padx=10)
button_2.place(relx=0.87,rely=0.03)


#v.config(command=.yview)

root_tk.mainloop()