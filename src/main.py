import audio_processing
import conversation


def main():
    # Create an instance of AudioProcessing
    audio = audio_processing.AudioProcessing()

    # Create an instance of Conversation
    conv = conversation.Conversation()

    while True:
        # Listen to the user's input
        user_input = audio.listen()

        # Process the user's input and get a response
        response = conv.process(user_input)

        # Speak the response
        audio.speak(response)


if __name__ == "__main__":
    main()
