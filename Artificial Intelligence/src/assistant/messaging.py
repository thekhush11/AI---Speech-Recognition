import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import speech_recognition as sr
import pyttsx3

def send_whatsapp_message(phone_no, message):
    try:
        import pywhatkit
        pywhatkit.sendwhatmsg_instantly(phone_no, message) # type: ignore
        return "WhatsApp message sent successfully!"
    except Exception as e:
        return f"Failed to send WhatsApp message: {str(e)}"

def send_email(subject, message, to_email):
    from_email = "vihaan110104@gmail.com"  
    password = "xlaq lsov lrfp cqjc"  

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

def listen_for_message(prompt="Listening for your message..."):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        audio = recognizer.listen(source)

    try:
        message = recognizer.recognize_google(audio) # type: ignore
        return message
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service."

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def handle_message_request():
    text_to_speech("What is the subject of your message?")
    subject = listen_for_message("Listening for the subject...")

    text_to_speech("What is the message?")
    message = listen_for_message("Listening for the message...")

    text_to_speech("Who should I send this message to?")
    to_email = listen_for_message("Listening for the recipient's email...")

    result = send_email(subject, message, to_email)
    text_to_speech(result)