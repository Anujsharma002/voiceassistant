import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language = 'en-In')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say That again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("who do you want to send message")
    speak('''option 1 - person with name
             option 2 - person with number''')
    a = int(input('option please:-'))
    speak("Whats Your message")
    message = str(input("Enter the message - "))
    if a ==1:
        num = int(input("Number:-"))
        #pywhatkit.sendwhatmsg(f"+91{num}",message,time_hour=strTime,time_min=update)
        pywhatkit.sendwhatmsg_instantly(f"+91{num}",message)
    else:
        name = input("Name:-")
        pywhatkit.sendwhatmsg_to_group_instantly(name,message)
