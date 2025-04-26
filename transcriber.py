import os
import whisper

RECORDINGS_DIR = "recordings"

# Convert audio to text
def transcribe_audio(filename):
    model = whisper.load_model("base")
    path = os.path.join(RECORDINGS_DIR, filename)
    try:
        result = model.transcribe(path)
        return result.get("text", "").strip()
    except Exception as e:
        print(f"Error: {e}")
        return None
