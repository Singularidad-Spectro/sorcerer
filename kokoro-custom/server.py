from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import base64
import os

app = FastAPI()

class TTSRequest(BaseModel):
    text: str
    voice: str
    language: str

@app.post("/tts")
async def generate_tts(request: TTSRequest):
    text = request.text
    voice = request.voice
    speed = 1.0  # Velocidad fija por ahora

    output_path = "/data/audio/output.mp3"

    try:
        # Ejecuta voicegen.py como subproceso
        subprocess.run(
            ["python", "/data/KOKORO/voicegen.py", text, voice, str(speed)],
            check=True
        )

        if not os.path.exists(output_path):
            raise HTTPException(status_code=500, detail="No se generó el archivo de audio")

        # Lee el archivo MP3 generado y conviértelo a base64
        with open(output_path, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode("utf-8")

        # Devuelve audio como base64
        return {
            "audio": audio_base64,
            "phonemes": f"Placeholder phonemes for '{text}'"
        }

    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Error al generar el audio")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))