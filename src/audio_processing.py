import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


class AudioProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()

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

    def speak(self, audio_text):
        print(audio_text)
        tts = gTTS(audio_text, 'en')
        tts.save("welcome.mp3")
        playsound("welcome.mp3")
