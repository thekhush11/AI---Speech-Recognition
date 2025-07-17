import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()
class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio) # type: ignore
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                self.speak("Sorry, I did not understand that.")
                return None
            except sr.RequestError:
                self.speak("Sorry, my speech service is down.")
                return None

    def get_audio_feedback(self, response):
        self.speak(response)