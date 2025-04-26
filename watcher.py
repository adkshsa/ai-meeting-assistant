import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from transcriber import transcribe_audio

RECORDINGS_DIR = "/app/recordings"

# Wait for file write completion
def wait_for_file_ready(filepath, timeout=30):
    start_time = time.time()
    while True:
        try:
            with open(filepath, "rb"):
                return True
        except Exception:
            time.sleep(1)
        if time.time() - start_time > timeout:
            return False

# Handle new recordings
class NewRecordingHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith((".mp4", ".mkv")):
            filename = os.path.basename(event.src_path)
            if wait_for_file_ready(event.src_path):
                transcribe_audio(filename)

# Start file watcher
def start_watching():
    os.makedirs(RECORDINGS_DIR, exist_ok=True)
    observer = Observer()
    observer.schedule(NewRecordingHandler(), path=RECORDINGS_DIR)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()
