import pyttsx3
import speech_recognition
import random

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

def game_play():
    speak("Lets Play Rock paper Scissor !!")
    print("lets playyyy")
    i = 0
    my_score = 0
    cam_score = 0
    while(i<5):
        choose = ("rock","paper","scissor")
        com_score = random.choice(choose)
        query = takeCommand().lower()
        i+=1
        if (query == "rock"):
            if(com_score == "rock"):
                speak("rock")
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
            elif (com_score == "paper"):
                speak("paper")
                cam_score +=1
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
            else:
                speak("Scissors")
                my_score +=1
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
        elif (query == "paper"):
            if(com_score == "paper"):
                speak("paper")
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
            elif (com_score == "scissor"):
                speak("scissor")
                cam_score +=1
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
            else:
                speak("rock")
                my_score +=1
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
        elif (query == "scissor"):
            if(com_score == "scissor"):
                speak("scissor")
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
            elif (com_score == "rock"):
                speak("rock")
                cam_score +=1
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
            else:
                speak("paper")
                my_score +=1
                print(f"{i}.Score:- Me :- {my_score}:Computer:-{cam_score}")
        elif "stop" in query:
            break
    if my_score > cam_score:
        speak(f"You won with {my_score} points")
    else:
        speak(f"You loose with {cam_score} points")