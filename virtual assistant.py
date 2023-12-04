import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Iam Virtual Assistant sir. Please tell me how may I help You")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("rajeswarisennamsetty@gmail.com","Password")
    server.sendmail("rajeswarisennamsetty@gmail.com",to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(f'{query}',sentences=5)
                speak("According to wikipedia")
                print(results)
                speak(resuls)
            except wikipedia.exceptions.PageError:
                pass
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'play music' in query:
            music_dir="D:\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time'in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")
        elif 'open code' in query:
            codepath="C:\projects"
            os.startfile(photopath)
        elif 'open photo' in query:
            photopath="D:\photos"
            os.startfile(photopath)
        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="rajeswarisennamsetty@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry,Iam not able to send this email")
        
    















        
        

