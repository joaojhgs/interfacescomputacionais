import whisper

# Load the whisper model
model = whisper.load_model("base")

# Path to the audio file
audio_path = "audio.mp3"

# Transcribe the audio file
result = model.transcribe(audio_path)

# Output the parsed audio content
print(result["text"])