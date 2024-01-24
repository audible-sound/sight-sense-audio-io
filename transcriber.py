import speech_recognition as sr 

def transcribeCommand(pause_threshold):
    # create new recogniser instance
    recogniser = sr.Recognizer()

    # connect to microphone
    with sr.Microphone() as audio_source:
        print("Listening......")
        # pause threshold -> minimum length of silence (in seconds) that will register as the end of a phrase
        recogniser.pause_threshold = pause_threshold
        # listen -> records a phrase from an audio source, returns an instance of AudioData
        audio_input = recogniser.listen(audio_source)

    try:
        print("Recognising user command.....")
        # method uses Google Speech Recognition API
        # API Key is generated automatically
        # Limited to 50 requests a day
        user_query = recogniser.recognize_google(audio_data = audio_input, language  = "en-GB")
        print(f"Transcription result: {user_query}")
    except Exception as exception:
        print("Unable to process user command.")
        print(exception)
        return "none"

    return user_query