# importing libraries

# pip install pyttsx3
import pyttsx3                    # text to speech
# pip install SpeechRecognition

import speech_recognition as sr   # speech to text

# robot voice

saying = pyttsx3.init()
voices = saying.getProperty('voices')
saying.setProperty('rate', 130)          # The speed of voice
saying.setProperty('voice', voices[1].id)  # 1 = woman  ||  0 = man


# text to speech function

def say(audio):
    saying.say(audio)
    saying.runAndWait()

say("Hello sir..... how can i help you")

# listen to user speech and say what he say

def listen():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as src:
            print("say something : ")
            audio = r.listen(src)
            US = r.recognize_google(audio, language="en-US")
            print("you said => " + US)
            say("you said .." + US)


try:
    listen()

except sr.UnknownValueError:
    listen()
