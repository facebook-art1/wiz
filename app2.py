import sys
import os
from gtts import gTTS
from tqdm import tqdm

def text_to_audio(txt_path, audio_path):
    try:
        # Open the text file and read its content
        with open(txt_path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()
        
        # Calculate the total number of chunks
        total_chunks = (len(text) + 19) // 20  # Round up to ensure last chunk is accounted for
        
        # Initialize progress bar
        with tqdm(total=total_chunks, desc="Converting to audio", unit="chunk") as pbar:
            # Initialize audio text pointer
            audio_pointer = 0
            # Process text in chunks
            while audio_pointer < len(text):
                # Extract a chunk of text
                chunk = text[audio_pointer:audio_pointer + 20]
                # Create a gTTS object for the chunk
                tts = gTTS(text=chunk, lang='en')
                # Save the audio to a file
                tts.save(audio_path, append=True)
                # Update progress bar
                pbar.update(1)
                # Move audio pointer to the next chunk
                audio_pointer += 20

        print(f"Audio file saved successfully: {audio_path}")
    
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
