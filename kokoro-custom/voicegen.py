import sys
import shutil
import os
from gradio_client import Client

# Configurar encoding si es necesario
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

# Obtener argumentos desde la línea de comandos
text = sys.argv[1]
voice = sys.argv[2]
speed = float(sys.argv[3])

print(f"Received text: {text}")
print(f"Voice: {voice}")
print(f"Speed: {speed}")

# Conectarse al servidor Gradio que expone la interfaz /tts
client = Client("http://kokoro-tts:7860/")

# Llamar a la función predict
result = client.predict(
    text=text,
    voice=voice,
    speed=speed,
    api_name="/tts"
)

# `result` es una tupla: (audio_path, phonemes)
audio_path = result[0]
phonemes = result[1]

# Ruta de salida donde Docker comparte volumen
output_path = "/data/audio/output.mp3"

# Asegurar que el directorio de destino exista
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Mover el archivo a la ruta compartida
shutil.move(audio_path, output_path)

# Imprimir fonemas (puede ser capturado por otros scripts si se requiere)
print(f"Phonemes: {phonemes}")