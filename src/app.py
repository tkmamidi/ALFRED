# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, _) = p.communicate()
   return output

# Initialize the recognizer
r = sr.Recognizer()
# engine.setProperty("rate", 150)  # Speed of speech (words per minute)
# engine.setProperty("volume", 0.8)  # Volume level (0.0 to 1.0)

# Function to convert text to
# speech
# def SpeakText(command):

## Initialize the engine
# engine = pyttsx3.init()
# engine.say(command)
# engine.runAndWait()


# Loop infinitely for user to
# speak

while 1:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            print("Listening...")
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ", MyText)
            # SpeakText(MyText)
            # add this for female voice -ven+f1 -k5 -s150
            c = 'espeak  --punct="<characters>" "%s" 2>>/dev/null' % MyText
            subprocess.Popen(c, stdout=subprocess.PIPE, shell=True).communicate()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
