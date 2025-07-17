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
    return recognizer, engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()

def listen_command(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        return command.lower()

def main():
    recognizer, engine = initialize_assistant()
    speak("Hello, I am Swaar. How can I help you today?", engine)

    while True:
        command = listen_command(recognizer)

        if "Tell me your name" in command:
            speak("I am your personalized voice assistant.", engine)
        elif "what time is it" in command: 
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}", engine)
        elif "what is the date" in command:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"Today's date is {current_date}", engine)
        elif "set a reminder" in command:
            result = set_reminder()
            speak(result, engine)
        elif "view reminders" in command:
            result = view_reminders()
            speak(result, engine)
        elif "delete reminder" in command:
            result = delete_reminder()
            speak(result, engine)
        elif "send message" in command:
            result = handle_message_request()
            speak(result, engine)
        elif "play music" in command:
            result = play_music(command)
            speak(result, engine)
        elif "what is" in command or "who is" in command:
            response = answer_query(command)
            speak(response, engine)
        elif "send whatsapp" in command:
            try:
                speak("Please say the phone number with country code.", engine)
                phone_no = listen_command(recognizer)
                speak("What is the message?", engine)
                message = listen_command(recognizer)
                result = send_whatsapp_message(phone_no, message)
                speak(result, engine)
            except Exception as e:
                speak("Sorry, I could not send the WhatsApp message. Please check your internet connection.", engine)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!, Have a nice day.", engine)
            break
        else:
            speak("I am sorry, I can't help with that.", engine)

if __name__ == "__main__":
    main()