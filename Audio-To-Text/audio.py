import speech_recognition as sr

def audio_to_text(file_path):
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        print("Processing audio file...")
        audio_data = recognizer.record(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print("Text from audio: {}".format(text))
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

# Use a raw string for the file path
audio_file_path = r'C:\Users\ASUS\OneDrive\Desktop\Audio\audio.wav'
audio_to_text(audio_file_path)
