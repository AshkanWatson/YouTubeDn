import tkinter
import customtkinter
from pytube import YouTube
import argparse
import sys
import os
from pytube.helpers import install_proxy



def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink , on_complete_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title , text_color='white')
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='Downloaded' , text_color='green')
    except:
        finishLabel.configure(text='field' , text_color='red')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_downloaded
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_compeletion) / 100 )

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('800x600')
app.title('Beta')

title = customtkinter.CTkLabel(app , text='enter Your URL Video')
title.pack(padx=10 , pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app , width=400 , height=30 , textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app , text='')
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app , text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

download = customtkinter.CTkButton(app , text='Download', command=startDownload)
download.pack(padx=10 , pady=10)


app.mainloop()