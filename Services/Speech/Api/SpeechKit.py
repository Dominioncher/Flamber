import json

from Core.Core import api
from Services.Speech.YandexSpeechKit import YandexSpeechKit as YaSpeech


@api.register('api/v1/speech_to_text')
def speech_to_text(audio: str) -> str:
    return YaSpeech.speech_to_text(audio)


@api.register('api/v1/text_to_speech')
def text_to_speech(text: str) -> str:
    return YaSpeech.text_to_speech(text)
