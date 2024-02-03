# Text to Speech program

# Description:
# This Python script utilizes the pyttsx3 library to create a simple Text-to-Speech (TTS) program.
# It defines a SpeakText function that takes text, rate, volume, and gender as parameters,
# allowing customization of speech output. The TTS engine initializes with specified settings
# and reads out the provided text using the selected voice.

# License:
# MIT License. Please do not claim as yours.

# Import the pyttsx3 library for text-to-speech functionality
import pyttsx3

# Function to convert text to speech
def SpeakText(command, Rate, Volume, Gender):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Adjust the speech rate based on the provided Rate parameter
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - Rate)

        # Set the volume level based on the provided Volume parameter
        volume = engine.getProperty('volume')
        engine.setProperty('volume', Volume)

        # Get available voices and set the TTS engine to use the specified gender voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[Gender].id)

        # Set the text to be spoken
        engine.say(command)
        print("Saying: " + command)

        # Wait for the speech to finish
        engine.runAndWait()

    except Exception as e:
        # Handle exceptions by printing a specific error message
        print(f"An error occurred: {e}")

# Example usage with sample parameters
SpeakText("Example", 1, 1, 0)
