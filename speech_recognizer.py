import speech_recognition
import pyttsx3
from time import sleep
from play_voice import voice

def recognize_speech(question): # can take in a question to ask before recognizing speech
    recognizer = speech_recognition.Recognizer()
    text = ""

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                if question:
                    voice(question)

                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                if text:
                    print(text)
                else:
                    print("nothing detected")
                return text

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue

    return ""

