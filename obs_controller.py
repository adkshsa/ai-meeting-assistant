import os
from obswebsocket import obsws, requests, exceptions
import time
from dotenv import load_dotenv
load_dotenv()

# Control OBS recording
def start_recording(recording_duration=60):
    host = os.getenv("OBS_HOST", "localhost")
    port = int(os.getenv("OBS_PORT", 4444))
    password = os.getenv("OBS_PASSWORD", "")

    client = None
    try:
        client = obsws(host, port, password)
        client.connect()
        client.call(requests.StartRecording()))
        time.sleep(recording_duration)
        client.call(requests.StopRecording()))
    except exceptions.ConnectionFailure:
        print("Connection failed")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if client:
            client.disconnect()

if __name__ == "__main__":
    start_recording()
