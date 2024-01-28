from transcriber import transcribeCommand
from speaker import speaker
from geopy.geocoders import Nominatim
import time

if __name__ == '__main__':
    speaker_rate = 150
    speaker_volume = 1 # 0 (min) to 1 (max)
    initial_greeting = "Welcome to SightSense!"
    id = "english" # select from available voice types offered by the machine
    speaker(initial_greeting, speaker_rate, speaker_volume, id)
    pause_threshold = 1.5 # interval in seconds
    activation_phrase = "hello"

    while True:
        activation_command = transcribeCommand(pause_threshold).lower()

        if activation_phrase in activation_command:
            time.sleep(0.25)
            speaker_prompt = "Hi! Where do you want to go?"
            speaker(speaker_prompt, speaker_rate, speaker_volume, id)
            while True:
                query = transcribeCommand(pause_threshold).lower()
                # Get directions
                # Stop Loop
                print(query)
                if query == "none":
                    continue
                elif "nevermind" in query:
                    speaker('Alright, goodbye', speaker_rate, speaker_volume, id)
                    break
                else:
                    # Establish connection to an API
                    geocoder = Nominatim(user_agent = "sightsense", timeout=10)
                    try:
                        location = geocoder.geocode(query)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    except Exception as exp:
                        print(exp)
                        print("Unable to fetch location")