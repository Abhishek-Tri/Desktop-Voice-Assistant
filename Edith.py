import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#this function will give voice output
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

    speak("I am Edith your voice assistant. Please tell me how can I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...") 
        speak("say that again please") 
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play kesariya' in query:
            try:
                dir = 'D:/music_dir'
                songs = os.listdir(dir)
                print(songs)    
                os.startfile(os.path.join(dir, songs[0]))
            except Exception as e:
                print(e)    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'sublime' in query:
            codePath = "D:\Sublime Text\sublime_text.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            speak("good by Abhishek Sir, i am taking a leave")
            print("Edith Terminated")
            exit() 

        elif 'search' in query:
            speak("tell me what you want to search?")
            query=takeCommand()
            speak("this is what i found")
            print("this is what i found")
            pywhatkit.search(query)
            
            try:
                result=wikipedia.summary(query,3)
                speak(result)
                print(result)

            except:
                speak("no speakable data available")

        elif 'screenshot' in query:
            pywhatkit.take_screenshot("automatic_ss",0,True)   
            speak("screenshot done successfully")     




           


