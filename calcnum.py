import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "A4AU94-TE884PGXK3"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("the value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("leo","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    final = str(Term)
    try:
        result = WolfRamAlpha(final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
