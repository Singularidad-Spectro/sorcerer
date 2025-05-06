#!/bin/sh

set -e

echo "Iniciando backend FastAPI..."
# Inicia el servidor en segundo plano
uvicorn server:app --host 0.0.0.0 --port 5000 &

echo "Iniciando puente Gradio..."
# Inicia la interfaz Gradio
python gradio_bridge.py