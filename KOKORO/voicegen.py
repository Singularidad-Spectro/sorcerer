import sys
import shutil
from gradio_client import Client
import os

# Set UTF-8 encoding for stdout (only needed in some Python 3.6-3.7)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

# Get arguments from command line
text = sys.argv[1]
voice = sys.argv[2]
speed = float(sys.argv[3])

print(f"Received text: {text}")
print(f"Voice: {voice}")
print(f"Speed: {speed}")

# Connect to local Gradio server (running in Docker at port 5000)
client = Client("http://kokoro-tts:7860/")

# Generate speech
result = client.predict(
    text=text,
    voice=voice,
    speed=speed,
    api_name="/tts"
)

# Define output path compatible with Docker volume
output_path = "/data/audio/output.mp3"

# Ensure destination directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Move generated file to shared volume
shutil.move(result[1], output_path)

print(f"Audio saved to {output_path}")
