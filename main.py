import speech_recognition as sr
import py

r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio, language="en-US")
            print(f"You said: {text}")
            return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def output(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    return

print("Listening... Press Ctrl+C to stop.")
while True:
    t = listen()
    if t:
        output(t)
        if "exit" in t.lower():
            print("Exiting...")
            break
        elif "help" in t.lower():
            print("How can I assist you?")
        elif "your name" in t.lower():
            print("I am a jarvis")
        else:
            print(f"im still learning idk abt ({t})")