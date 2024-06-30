import datetime
import os
import subprocess
import time
import webbrowser
import pytypes
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import smtplib
import pyjokes
import winshell
import wolframalpha
from django.contrib.sites import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir I am Mark how may I help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query


def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login('21BCS1662@cuchd.in', 'ronitRAJIB@123')
    server.sendmail('21BCS1662@cuchd.in',to , content)
    server.close()


if __name__ == "__main__":

    wishMe()

    if 1:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("what's next sir")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open music' in query:
            music_dir = 'C:\\Users\\lenovo\\Videos\\Captures'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'how are you' in query:
            speak("I am fine,Thank You")
            speak("How are you,Sir")

        elif 'fine' in query:
            speak("It's good to know that you are fine")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by RONIT.")
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif "what is" in query or "who is" in query:
            speak("I can answer to computational and geographical question and what question do you want to ask now")
            content = takeCommand()
            aap_id = "HKJEUA-2KW4AA5WRJ"
            client = wolframalpha.Client("HKJEUA-2KW4AA5WRJ")
            res = client.query(content)
            answer = next(res.results).txt
            speak(answer)
            print(answer)
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "21BCS2472@cuchd.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ronit . I am not able to send this email")


        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif "weather" in query:

            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")


