import pyttsx3

engine = pyttsx3.init()

# list out available voice types
def voice_types():
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice)

def speaker(text, speaker_rate, volume, id):
    # set the speed of speaker
    engine.setProperty('rate', speaker_rate)
    # adjust volume
    engine.setProperty('volume', volume)
    # change speaker
    engine.setProperty('voice', id)
    engine.say(text)
    engine.runAndWait()