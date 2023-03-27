import time

import pyttsx3
# initialize the TTS engine
engine = pyttsx3.init()

# set properties for the engine
engine.setProperty('rate', 150) # speed of speech (words per minute)
engine.setProperty('volume', 0.9) # volume (0 to 1)

# specify the text to be spoken

# speak the text
def say(text):
    engine.say(text)
    print('fgg')
    engine.stop()


tts =_TTS()
tts.start("text")
#del(tts)