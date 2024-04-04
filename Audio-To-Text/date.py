import speech_recognition as sr
from dateutil import parser

def extract_date_from_audio(audio_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    # Recognize speech
    try:
        text = recognizer.recognize_google(audio_data)
        print("Recognized speech:", text)
        
        # Parse date from recognized speech
        date = parser.parse(text, fuzzy=True).date()
        return date

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("An error occurred: {0}".format(e))

# Replace 'your_audio_file.wav' with the path to your audio file
audio_file = 'audio.wav'
date = extract_date_from_audio(audio_file)
if date:
    formatted_date = date.strftime("%d/%m/%Y")
    print("The date is:", formatted_date)
