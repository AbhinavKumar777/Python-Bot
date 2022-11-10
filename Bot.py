from ast import main
from dataclasses import replace
import datetime
from email import message
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import Automations
""" This is to Open Brave"""
# from selenium import webdriver
# driver_path = "C:/Users/username/PycharmProjects/chromedriver.exe"
# brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
# option = webdriver.ChromeOptions()
# option.binary_location = brave_path
# # option.add_argument("--incognito") OPTIONAL
# # option.add_argument("--headless") OPTIONAL

# # Create new Instance of Chrome
# browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
""" Till here"""

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")


def takecommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User Input: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        return "None"
    return query


def GoogleSearch(term):
    Query=str(term)
    pywhatkit.search(Query)


def youtubesearch(term):
    ytlink = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(ytlink)
    # pywhatkit.playonyt(term)


def Ytdownload():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    from pyperclip import paste
    from time import sleep
    import pyautogui

    sleep(3)
    kkk = pyautogui.position()
    click(kkk)
    hotkey('ctrl','c')
    value = paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('C:\\Users\\DCGLocalAdmin\\Desktop\\')

    Download(Link)
    speak("Task Positive")
    os.startfile("C:\\Users\\DCGLocalAdmin\\Desktop\\")


def sendemail(to, content):
# Enable less secure apps on Gmail to be able to send
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password-here")
    # Save your password in a Text file and return it here
    server.sendmail("youremail@gmail.com",to, content)
    server.close()


if __name__ == "__main__":
    wish_me()
    while True:
        query = takecommand().lower()
        
        # Tasks Logic
        if 'quit' in query:
            exit()
 
        elif 'youtube' in query:
            if  "search" in query:
                try:
                    query = query.replace("youtube","")
                    query = query.replace("search","")
                    youtubesearch(query)
                except Exception as e:
                    speak("Negative")
            else:
                templink ="https://www.youtube.com/"
                webbrowser.open(templink)

        elif "whatsapp" in query:
            query = query.replace("whatsapp","")
            if "chat" in query:
                query = query.replace("show","")
                query = query.replace("chat","")
                Automations.WhatsappChat(query)

            elif "message" in query:
                query = query.replace("message","")
                query = query.replace("send","")
                query = query.replace("to","")
                speak(f"Meassage please {query}")
                text = takecommand()
                Automations.WhatsappMsg(query,text)

            elif "call" in query:
                query = query.replace("Send","")
                query = query.replace("call","")
                query = query.replace("to","")
                Automations.WhatsappCall(query)

        elif 'open spotify' in query:
            Spotify_Path = "C:\\Users\\DCGLocalAdmin\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(Spotify_Path)

        elif 'google' in query:
            # speak("Mode")
            # term=takecommand().lower()
            # if "normal" in term:
            #     templink="https://www.google.com/"
            #     webbrowser.open(templink)
            # else:
            #     try:
            #         GoogleSearch(term)
            #     except Exception as e:
            #         speak("Task Negative") 
            query = query.replace("google", "")
            try:
                GoogleSearch(query)
            except Exception as e:
                speak("Task Negative")

        elif 'download this video' in query:
            Ytdownload()

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(strTime)

        elif 'vs code' in query:
            vs_code_path = "C:\\Users\\DCGLocalAdmin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_code_path)

        elif 'send email to ak' in query:
            # Make a dictionary and store the persons
            # key as their Addess
            '''person = takecommand().lower()
            if 'ak' in person:
                speak("Tarvatha choodham le")'''
            try:
                speak("Content?")
                content = takecommand()
                to = "toemail@gmail.com"
                sendemail(to, content)
                speak("Positive")
            except Exception as e:
                print(e)
                speak("Negative")

