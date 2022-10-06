import pyaudio
import pyttsx3
from multiprocessing.connection import Listener
import speech_recognition as sr

listener = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    voice = listener.listen(source)
    command = listener.recognize(voice)
    print(command)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("how are you doing")
engine.runAndWait()