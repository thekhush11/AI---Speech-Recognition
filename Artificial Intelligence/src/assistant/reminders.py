import datetime

reminders = []

def set_reminder():
    from main import speak, listen_command, initialize_assistant
    recognizer, engine = initialize_assistant()
    speak("What should I remind you about?", engine)
    reminder_text = listen_command(recognizer)
    speak("When should I remind you? Please say the time in HH:MM format.", engine)
    reminder_time = listen_command(recognizer)
    reminders.append({"text": reminder_text, "time": reminder_time})
    return f"Reminder set for {reminder_time}: {reminder_text}"

def view_reminders():
    if not reminders:
        return "You have no reminders."
    result = "Your reminders are: "
    for idx, rem in enumerate(reminders, 1):
        result += f"\n{idx}. {rem['text']} at {rem['time']}"
    return result

def delete_reminder():
    from main import speak, listen_command, initialize_assistant
    recognizer, engine = initialize_assistant()
    if not reminders:
        return "You have no reminders to delete."
    speak("Which reminder number do you want to delete?", engine)
    reminder_number = listen_command(recognizer)
    try:
        idx = int(reminder_number) - 1
        removed = reminders.pop(idx)
        return f"Deleted reminder: {removed['text']} at {removed['time']}"
    except:
        return "Invalid reminder number."