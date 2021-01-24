import pyttsx3
import speech_recognition as sr
import pyaudio

def get():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something')
        audio=r.listen(source)
        print('done!')


    try:
        text = r.recognize_google(audio)
        print(text)

    except Exception as e:
        print(e)


get()