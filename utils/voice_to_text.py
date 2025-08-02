import speech_recognition as sr
from pydub import AudioSegment
import io

def transcribe_audio(audio_bytes, out_wav_path):
    # audio_bytes is bytes
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    audio.export(out_wav_path, format="wav")
    r = sr.Recognizer()
    with sr.AudioFile(out_wav_path) as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data, language="en-IN")
        return text
    except Exception:
        return ""