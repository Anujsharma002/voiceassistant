import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d35ea4fb9d294213a3ecb931c991f768",
                "entertainment":"https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=d35ea4fb9d294213a3ecb931c991f768"
                , "healt":"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=d35ea4fb9d294213a3ecb931c991f768",
                "science":"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=d35ea4fb9d294213a3ecb931c991f768",
                "sports":"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=d35ea4fb9d294213a3ecb931c991f768"
                ,"technology":"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=d35ea4fb9d294213a3ecb931c991f768"
                }
    content = None
    url = None
    speak("Which field news do you want,[business],[health],[technology],[sports],[entertainment],[science]")
    field = input("Type field news that you want:")
    for key , value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for artiicles in arts:
        artiicle = artiicles["title"]
        print(artiicle)
        speak(artiicle)
        news_url = artiicles["url"]
        print(f"for more info visit:{ news_url }")

        a = input("[press 1 to continue] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

        speak("thats all")