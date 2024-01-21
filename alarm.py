import pyttsx3
import datetime
import os
from playsound import playsound
from pygame import mixer
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtxt.txt","r")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtxt.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset =  str(time)
    timenow = timeset.replace("leo","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
          speak("Alarm ringing,sir")
          mixer.init()
          mixer.music.load("D:\songs\iphone_sound.mp3")
          mixer.music.play()


        elif currenttime + "00:00:30" == Alarmtime:
            exit()

        ring(time)

