import speech_recognition as sr
import pyttsx3
import datetime
from assistant.reminders import set_reminder, view_reminders, delete_reminder
from assistant.messaging import handle_message_request, send_whatsapp_message
from assistant.music import play_music
from assistant.queries import answer_query

def initialize_assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    return recognizer, engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()

def listen_command(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

if __name__ == "__main__":
    recognizer, engine = initialize_assistant()
    speak("Hello, I am Swaar, how can I help you today?", engine)

    while True:
        command = listen_command(recognizer)

        if not command:
            speak("I didn't catch that. Please try again.", engine)
            continue

        if "name" in command:
            speak("I am Swaar, your personalized voice assistant.", engine)

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}", engine)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"Today's date is {current_date}", engine)

        elif "reminder" in command and "set" in command:
            result = set_reminder()
            speak(result, engine)

        elif "reminder" in command and "view" in command:
            result = view_reminders()
            speak(result, engine)

        elif "reminder" in command and "delete" in command:
            result = delete_reminder()
            speak(result, engine)

        elif "message" in command or "text" in command:
            result = handle_message_request()
            speak(result, engine)

        elif "music" in command or "play song" in command or "play music" in command:
            result = play_music(command)
            speak(result, engine)

        elif "who is" in command or "what is" in command:
            response = answer_query(command)
            speak(response, engine)

        elif "whatsapp" in command and "send" in command:
            speak("Please say the phone number.", engine)
            phone_no = listen_command(recognizer)
            speak("Please say the message you want to send.", engine)
            message = listen_command(recognizer)
            result = send_whatsapp_message(phone_no, message)
            speak(result, engine)

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.", engine)
            break

        else:
            speak("Sorry, I didn't understand that. Try again.", engine)