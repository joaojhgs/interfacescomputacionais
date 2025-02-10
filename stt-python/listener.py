import whisper
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please speak...")
    audio = recognizer.listen(source)
    print("Recording finished.")

# Save the captured audio to a file
audio_path = "output.wav"
with open(audio_path, "wb") as f:
    f.write(audio.get_wav_data())

# Load the whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe(audio_path)

# Output the parsed audio content
print(result["text"])