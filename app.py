import sys
import os
import time
import pyttsx3
from tqdm import tqdm

def text_to_audio(txt_path, audio_path):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

        # Open the text file and read its content
        with open(txt_path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()

        # Calculate the total number of characters
        total_chars = len(text)

        # Initialize audio pointer
        audio_pointer = 0

        # Start conversion process
        with open(audio_path, 'wb') as audio_file:
            with tqdm(total=total_chars, desc="Converting to audio", unit="chars") as pbar:
                while audio_pointer < total_chars:
                    # Extract a chunk of text
                    chunk = text[audio_pointer:audio_pointer + 20]
                    audio_pointer += len(chunk)

                    # Speak the chunk
                    engine.say(chunk)

                    # Wait for the chunk to be spoken
                    engine.runAndWait()

                    # Update progress
                    pbar.update(len(chunk))

                    # Artificial delay for demonstration purposes (remove or adjust as needed)
                    time.sleep(0.1)

            print(f"\nAudio file saved successfully: {audio_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 app.py <input_txt_file> <output_audio_file>")
        sys.exit(1)

    # Get the input and output file paths from command line arguments
    input_txt_file = sys.argv[1]
    output_audio_file = sys.argv[2]

    # Check if the input text file exists
    if not os.path.exists(input_txt_file):
        print(f"Error: Input text file '{input_txt_file}' not found")
        sys.exit(1)

    # Convert text to audio and save it to the audio file
    text_to_audio(input_txt_file, output_audio_file)
