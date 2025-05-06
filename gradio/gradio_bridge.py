import gradio as gr
import requests
import base64
import tempfile

def generate_speech(text, voice, speed):
    # FastAPI endpoint de tu app (adaptar si usas otra ruta o puerto)
    url = "http://localhost:5000/tts"
    language = "b" if voice == "george" else "a"

    try:
        response = requests.post(url, json={
            "text": text,
            "voice": voice,
            "language": language
        })
        response.raise_for_status()
        data = response.json()
        audio_base64 = data["audio"]
        phonemes = data["phonemes"]

        # Decodificar base64 y guardar como archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav", mode="wb") as tmpfile:
            tmpfile.write(base64.b64decode(audio_base64))
            filepath = tmpfile.name

        # Retornar ruta del archivo generado y los fonemas
        return filepath, phonemes

    except Exception as e:
        return None, f"Error: {str(e)}"

iface = gr.Interface(
    fn=generate_speech,
    inputs=[
        gr.Textbox(label="Text"),
        gr.Dropdown(choices=["default", "sarah", "bella", "george", "michael"], label="Voice"),
        gr.Slider(minimum=0.5, maximum=2.0, step=0.1, value=1.0, label="Speed")
    ],
    outputs=[
        gr.Audio(label="Generated Audio", type="filepath"),
        gr.Textbox(label="Phonemes")
    ],
    title="Kokoro TTS Bridge",
    description="Bridge for gradio_client compatibility",
)

# Iniciar interfaz en la red local (puerto 7860)
iface.launch(server_name="0.0.0.0", server_port=7860)
