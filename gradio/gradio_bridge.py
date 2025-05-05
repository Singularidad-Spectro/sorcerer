import gradio as gr
import requests

def generate_speech(text, voice, speed):
    # FastAPI endpoint de tu app
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

        # Devolver en formato Gradio
        return f"data:audio/wav;base64,{audio_base64}", phonemes

    except Exception as e:
        return None, f"Error: {str(e)}"

iface = gr.Interface(
    fn=generate_speech,
    inputs=[
        gr.Textbox(label="Text"),
        gr.Dropdown(choices=["default", "sarah", "bella", "george", "michael"], label="Voice"),
        gr.Slider(minimum=0.5, maximum=2.0, step=0.1, value=1.0, label="Speed")  # aunque el backend no lo usa aún
    ],
    outputs=[
        gr.Audio(label="Generated Audio", type="filepath"),
        gr.Textbox(label="Phonemes")
    ],
    title="Kokoro TTS Bridge",
    description="Bridge for gradio_client compatibility"
)

iface.launch(server_name="0.0.0.0", server_port=7860)