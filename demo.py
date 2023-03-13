import pyttsx3

# initialize the TTS engine
engine = pyttsx3.init()

# set properties for the engine
engine.setProperty('rate', 150) # speed of speech (words per minute)
engine.setProperty('volume', 0.9) # volume (0 to 1)

# specify the text to be spoken
text = "Hello, world! This is a sample text."

# speak the text
def say(text):
    engine.say(text)

    # start the TTS engine and wait until the text has been spoken
    engine.runAndWait()