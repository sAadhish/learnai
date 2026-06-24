from faster_whisper import WhisperModel
from pprint import pprint
model=WhisperModel('base',device="cpu")
segments,info=model.transcribe("day10/LLM.m4a")
for segment in segments:
    pprint(segment.text)