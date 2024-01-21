from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("460x360")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    root.attributes('-alpha',0.7)
    global img
    img = Image.open(r"C:\Users\anujs\Downloads\jarvis.gif")
    lb1 = Label(root)
    lb1.place(x=0,y=0)
    i=0
    mixer.music.load(r"C:\Users\anujs\Downloads\load.mp3")
    mixer.music.play()
    time.sleep(0.2)
    mixer.music.stop()
    for img in ImageSequence.Iterator(img):
        img = img.resize((460,360))
        img = ImageTk.PhotoImage(img)
        lb1.config(image=img,background=None)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()
