import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You said:", command)
            return command

        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

        except sr.RequestError:
            print("Internet connection error")
            return ""

        except Exception as e:
            print("Error:", e)
            return ""

speak("Hello, I am Oreo, your voice assistant.")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello, how are you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        engine.say(f"The current time is {current_time}")
        engine.runAndWait()

    elif "date" in command:
        today = datetime.date.today()
        engine.say(f"Today's date is {today}")
        engine.runAndWait()

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        engine.say("Opening Google")
        engine.runAndWait()

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        engine.say("Opening YouTube")
        engine.runAndWait()

    elif "back to vs code" in command:
        webbrowser.open("C:\\Users\\Bipransu\\OneDrive\\Desktop\\PROJECT OASIS INFOBYTE\\VoiceAssistant.py")

    elif "exit" in command or "stop" in command:
        engine.say("Goodbye! Have a nice day.")
        engine.runAndWait()
        break

    elif command != "":
        engine.say("Sorry, I didn't understand that command.")
        engine.runAndWait()
