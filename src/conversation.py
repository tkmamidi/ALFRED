import speech_recognition as sr
from audio_processing import AudioProcessing


class Conversation:
    def __init__(self):
        self.audio_processing = AudioProcessing()
        self.recognizer = sr.Recognizer()

    def process(self, audio):
        print(audio)
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except Exception as e:
            print("Sorry, I did not get that (process). Could you please repeat?")
            return None

    def respond(self, text):
        if text:
            self.audio_processing.speak(text)
        else:
            self.audio_processing.speak(
                "Sorry, I did not get that. Could you please repeat?"
            )
