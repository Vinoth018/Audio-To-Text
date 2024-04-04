# from gtts import gTTS

# def text_to_speech(text, filename='output.wav'):
#     tts = gTTS(text=text, lang='en')  # You can specify language here, 'en' for English
#     tts.save(filename)
#     print(f"Text converted to audio. Saved as {filename}")

# if __name__ == "__main__":
#     text = input("Enter the text you want to convert to audio: ")
#     filename = input("Enter the filename to save as (include .wav extension): ")
#     text_to_speech(text, filename)










# import pyttsx3
# import os

# def text_to_speech(text, output_path):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()
    
#     # Set properties, including saving to a .wav file
#     engine.setProperty('rate', 150)  # Speed of speech
#     engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)

#     # Save to a .wav file
#     engine.save_to_file(text, output_path)
    
#     # Run the engine (without this, speech will not be audible)
#     engine.runAndWait()

# if __name__ == "__main__":
#     text = "Hello, this is Harikaran, i am a python developer , i have joined app experts accademy in 23rd august 2023"
#     output_path = "output.wav"
#     text_to_speech(text, output_path)
#     print(f"Speech saved as {output_path}")









import pyttsx3
import os

def text_to_speech(text, output_path):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties, including saving to a .wav file
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)

    # Save to a .wav file
    engine.save_to_file(text, output_path)
    
    # Run the engine (without this, speech will not be audible)
    engine.runAndWait()

if __name__ == "__main__":
    # Prompt the user to input the text
    text = input("Enter the text to convert to speech: ")
    
    # Set the output path
    output_path = "output.wav"
    
    # Call the text_to_speech function
    text_to_speech(text, output_path)
    
    print(f"Speech saved as {output_path}")
