import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import re
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Livewire. I am your personal assitant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio=r.record(source, duration = 4)
        print(audio)
        #audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: {0}\n".format(query))

    except Exception:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('himanisarathebce15@gmail.com', 'sonisonisushil')
#     server.sendmail('himanisarathebce15@gmail.com', to, content)
#     server.quit()

if __name__ == "__main__":
    wishMe()
    sss=input('Press any key to start Livewire Chatbot')
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search engine' in query:
            speak('Press any key when you are ready to speak')
            key=input()
            while True:
                query=''
                query = takeCommand().lower()
                if(query=='search engine exit'):
                    break
                try:
                    results = wikipedia.summary(query, sentences=2)
                except:
                    print('please retry')
                speak("According to my knowledge")
                print(results)
                speak(results)
                
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open college website' in query:
               webbrowser.open("https://bgibhopal.com/bist/")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {}".format(strTime))

        elif 'open code' in query:
            codePath = "C:\\Users\\"
            os.startfile(codePath)

        # elif 'email to himani' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "himanisarathebce15@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend . I am not able to send this email")    
        # elif 'exit' in query:
            break