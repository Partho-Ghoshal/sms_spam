import os
from vosk import Model, KaldiRecognizer
import wave

def transcribe_video(file_path):
    # Load the Vosk model
    model = Model("model")  # Download Vosk's English model from https://alphacephei.com/vosk/models
    wf = wave.open(file_path, "rb")
    
    # Initialize recognizer
    recognizer = KaldiRecognizer(model, wf.getframerate())
    
    transcription = []
    while True:
        data = wf.read(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            transcription.append(result)
    
    return ' '.join(transcription)
