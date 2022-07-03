import speech_recognition

class SpeechToText():
    MICRO_TIMEOUT = 2
    MICRO_PHRASE_MAXLEN = 5
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.micro = speech_recognition.Microphone()
    
    def get_text(self, audio):
        return self.recognizer.recognize_google(audio, language='ru')
