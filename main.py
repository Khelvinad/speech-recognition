import speech_recognition as sr
import asyncio
import os
from edge_tts import Communicate
from playsound import playsound

VOICE = "zh-CN-YunxiaNeural" 
OUTPUT_FILE = "response.mp3"

r = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

async def speak_async(text):
    print(f"Jarvis: {text}")
    try:
        communicate = Communicate(text, VOICE)
        await communicate.save(OUTPUT_FILE)
        playsound(OUTPUT_FILE)
    except Exception as e:
        print(f"An error occurred during speech synthesis: {e}")
    finally:
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)

def speak(text):
    try:
        asyncio.run(speak_async(text))
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(speak_async(text))



try:
    while True:
        user_input = listen()

        if user_input:
            response_text = ""
            user_input_lower = user_input.lower()

            if "your name" in user_input_lower or "nama" in user_input_lower:
                response_text = "supp my name is Jarvis. what about you?"
            elif "hallo" in user_input_lower or "hi" in user_input_lower or "help" in user_input_lower:
                response_text = "supp gang need something?"
            elif "my name" in user_input_lower:
                name = user_input_lower.split("my name is")[-1].strip()
                response_text = f"nice to meet you {name}"
            elif "weather" in user_input_lower:
                response_text = "we dont care about the fucking weather man"
            elif "exit" in user_input_lower or "stop" in user_input_lower:
                response_text = "adios gang"
                speak(response_text)
                break
            elif "play" in user_input_lower:
                response_text = "lets rocking gang"
                speak(response_text)
                playsound(r'C:\Users\khelv\Downloads\tambalban.mp3')
            else:
                response_text = f"im stil learning idk abt: {user_input}"


            if response_text:
                speak(response_text)

except KeyboardInterrupt:
    print("\nStopping...")
finally:
    print("Exit.")