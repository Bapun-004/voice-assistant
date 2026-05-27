import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You said:", command)
            return command

        except:
            return ""
speak("Hello, I am oreo, your voice assistant")

while True:

    command = take_command()

    if "hello" in command:
        speak("Hello, how are you")

        if "i am fine" in command:
            speak("That's great to hear")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current_time)
    
    elif "date" in command:
        today = datetime.date.today()
        speak("Today's date is " + str(today))
    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break
    elif command != "":
        speak("Command not found")