import pyttsx3
import speech_recognition as sr
import datatime
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour > 0 and hour < 12):
        speak("Good morning,sir")
    elif (hour > 12 and hour < 18):
        speak("Good afternoon ,sir")
    else:
        speak("Good evening , sir")
    speak(
        "Its sirius , How can i help you")


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1.5)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":

    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("All right sir, as you say , Searching in Wikipedia....")
            query = query.replace("wikipedia", ' ')
            results = wikipedia.summary(query, sentences=2)
            speak("Well ,I read it all but the important thing I got is ")
            speak(results)


        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open Facebook" in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif "open Linkedin" in query:
            webbrowser.open("Linkedin.com")

        elif "open Github" in query:

            webbrowser.open("Github.com")


        elif ' sleep' in query:
            break