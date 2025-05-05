#!/bin/bash
# Inicia el backend de Kokoro TTS
uvicorn server:app --host 0.0.0.0 --port 5000 &

# Esperar unos segundos para asegurar que el servidor esté arriba antes de lanzar Gradio
sleep 10

# Inicia la interfaz Gradio
python gradio_bridge.py