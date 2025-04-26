import subprocess
import os
from transcriber import transcribe_audio
from summarizer import summarize_meeting

RECORDINGS_DIR = "recordings"
TRANSCRIPTS_DIR = "transcripts"
SUMMARIES_DIR = "summaries"

import glob
import time

# Get most recent recording
def get_latest_recording():
    files = glob.glob(os.path.join(RECORDINGS_DIR, "*.mkv"))
    if not files:
        raise Exception("No recordings found")
    files.sort(key=os.path.getmtime, reverse=True)
    return os.path.basename(files[0])

# Main pipeline
def main():
    print("Starting meeting assistant pipeline")

    # Record meeting
    subprocess.run(["python", "obs_controller.py"])
    
    # Process recording
    latest_file = get_latest_recording()
    transcript = transcribe_audio(latest_file)
    
    if not transcript:
        return

    summary = summarize_meeting(transcript)

    # Save outputs
    base = os.path.splitext(latest_file)[0]
    with open(os.path.join(TRANSCRIPTS_DIR, f"{base}.txt"), "w") as f:
        f.write(transcript)
    with open(os.path.join(SUMMARIES_DIR, f"{base}.summary.txt"), "w") as f:
        f.write(summary)

if __name__ == "__main__":
    main()
