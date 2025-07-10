from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from TTS.api import TTS
import uuid

app = FastAPI()

# Load Coqui TTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

@app.get("/speak")
def speak(text: str = Query(...)):
    output_path = f"{uuid.uuid4().hex}.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return FileResponse(output_path, media_type="audio/wav", filename="speech.wav")

@app.get("/")
def root():
    return {"message": "Welcome to Coqui TTS API. Use /speak?text=Hello"}
