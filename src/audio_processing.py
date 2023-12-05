import speech_recognition as sr
import pyttsx3


class AudioProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
