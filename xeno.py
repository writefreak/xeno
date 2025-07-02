import speech_recognition as sr
import pyttsx3
import pyautogui
import subprocess
import datetime




def listen_to_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there's an error with the speech service.")
        return None
    


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_time_based_greeting():
    # Get the current hour from the system's clock
    current_hour = datetime.datetime.now().hour

    # Determine the time of day and return a personalized greeting
    if 0 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
    

def open_spotify():
    subprocess.run(["spotify"])

def open_chrome():
    # Use the full path to Chrome executable
    subprocess.run([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])

def close_chrome():
    pyautogui.hotkey("ctrl", "w")  # Close current tab

def process_command(command):
    if "open spotify" in command:
        open_spotify()
        speak("Opening Spotify.")
    elif "open chrome" in command:
        open_chrome()
        speak("Opening Chrome.")
    elif "close chrome" in command:
        close_chrome()
        speak("Closing Chrome.")
    else:
        speak("I didn't catch that. Can you say it again?")

def main():
    speak(get_time_based_greeting()) 
    speak("Hello Heritage, I'm Xeno. How can I assist you today?")
    while True:
        command = listen_to_command()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
