import os
import random
import webbrowser
import speedtest
import pyautogui
import pyttsx3
import requests
import speech_recognition
from bs4 import BeautifulSoup
import datetime
import pyautogui
from plyer import notification
from pygame import mixer
from instrogif import play_gif

for i in range(3):
    a = input("Enter Password to open jarvis:-")
    pw_file = open("pop.txt","r")
    pw = pw_file.read()
    pw_file.close()
    #if ( pw == ''):
     #   pw_file = open("pop.txt","w")
      #  pw = pw_file.write(a)
       # pw_file.close()
    if (a==pw):
        print("Welcome sir ! please speak [wake up] to load me up")
        break
    elif (i == 2 and a!=pw):
         exit()

    elif (a!=pw):
        print("Try Again")


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

def alarm(query):
    timewhere = open("Alarmtxt.txt","a")
    timewhere.write(query)
    timewhere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in  query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call anytime")
                    break

                elif "translate" in query:
                    from Translator import translategl

                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("pop.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode:-[1 for Yes/ 2 for No]"))
                    if (a == 1):
                        speak("Entering the focus Mode.....")
                        os.startfile("C:\\Users\\anujs\\PycharmProjects\\voiceassist\\restriction.py")

                        exit()




                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (please speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("schedule.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks:-"))
                        i=0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("schedule.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        no_tasks = int(input("Enter the no. of tasks:-"))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("schedule.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("schedule.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("D:\songs\iphone_sound.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule:-",
                        message = content,
                        timeout = 15
                    )
                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save(r"C:\Users\anujs\OneDrive\Pictures\aj.jpg")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile")
                    pyautogui.press("enter")

                elif "hello" in query:
                    speak("Hello sir, how are you")
                elif "i am fine" in query:
                    speak("that's, great sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("Your are Welcome sir")

                elif "tired" in query:
                    speak("Playing your favourite songs , sir")
                    a = (1,2,3,4)
                    b = random.choice(a)
                    if b ==1 :
                        webbrowser.open("https://www.youtube.com/watch?v=btPJPFnesV4")
                    elif b ==2:
                        webbrowser.open("https://www.youtube.com/watch?v=Tom5AVbJ_2g")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
                    elif b == 4:
                        webbrowser.open("https://www.youtube.com/watch?v=TO-_3tck2tg")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video is muted")
                elif "skip forward" in query:
                    pyautogui.press("l")
                elif "skip backward" in query:
                    pyautogui.press("j")
                elif "full" in query:
                    pyautogui.press("f")
                elif "mini" in query:
                    pyautogui.press("f")
                elif "minimize" in query:
                    pyautogui.press("i")
                elif "undo minimize" in query:
                    pyautogui.press("i")
                elif "show my focus" in query:
                    from focus import focus_graph
                    focus_graph()



                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down , sir")
                    volumedown()

                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("leo","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")
                #elif "open" in query:
                  #  from Dictapp import openappweb
                   # openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576
                    download_net = wifi.download()/1048576
                    print("Wifi upload speed is",upload_net)
                    print("Wifi download speed is",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi upload speed is {upload_net}")

                elif "ipl score" in query:
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    from bs4 import BeautifulSoup
                   # team1 = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()
                    #team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()
                    team1 =1
                    team2=2
                    a = print(f"{team1}:{team1_score}")
                    b = print(f"{team2}:{team2_score}")

                    notification.notify(
                        title = "Ipl score:-",
                        message = f"{team1}:{team1_score}/n{team1}:{team1_score}",
                        timeout = 15
                    )

                elif "start a game" in query:
                    from game import game_play
                    game_play()
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from calcnum import WolfRamAlpha
                    from calcnum import Calc
                    query = query.replace("calculate","")
                    query = query.replace("leo","")
                    Calc(query)

                elif "whatsapp" in query:
                    from whatsapp import sendMessage
                    sendMessage()
                elif "temperature" in query:
                    search = "temperature in gwalior"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in gwalior"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done ,Sir")


                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("leo","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to " + remember.read())
                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break