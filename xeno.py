import speech_recognition as sr
import pyttsx3
import pyautogui
import subprocess
import datetime
import json
import os
import time
import sys

# Simple memory file path
MEMORY_FILE = "xeno_memory.json"

# Load or initialize memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)
else:
    memory = {
        "name": "Heritage",
        "fav_color": "blue"
    }

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🧠 Command received: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Sorry, there's a problem with the speech service.")
        return None

def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# 💥 Original hardcoded app openers with logging for debugging
def open_chrome():
    try:
        print("Attempting to open Chrome...")
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe", shell=True)
        speak("Opening Chrome.")
        print("Chrome opened successfully!")
    except Exception as e:
        print(f"Error opening Chrome: {e}")
        speak("Failed to open Chrome.")

def open_vscode():
    try:
        print("Attempting to open Visual Studio Code...")
        subprocess.Popen(r"C:\Users\Pc\AppData\Local\Programs\Microsoft VS Code\Code.exe", shell=True)
        speak("Opening Visual Studio Code.")
        print("VS Code opened successfully!")
    except Exception as e:
        print(f"Error opening VS Code: {e}")
        speak("Failed to open Visual Studio Code.")

def open_github_desktop():
    try:
        print("Attempting to open GitHub Desktop...")
        subprocess.Popen(r"C:\Users\Pc\AppData\Local\GitHubDesktop\GitHubDesktop.exe", shell=True)
        speak("Opening GitHub Desktop.")
        print("GitHub Desktop opened successfully!")
    except Exception as e:
        print(f"Error opening GitHub Desktop: {e}")
        speak("Failed to open GitHub Desktop.")

def open_file_explorer():
    try:
        print("Attempting to open File Explorer...")
        subprocess.Popen(r"C:\Windows\explorer.exe", shell=True)
        speak("Opening File Explorer.")
        print("File Explorer opened successfully!")
    except Exception as e:
        print(f"Error opening File Explorer: {e}")
        speak("Failed to open File Explorer.")

def open_start_menu():
    try:
        print("Attempting to open Start Menu...")
        pyautogui.press("win")
        speak("Opening Start Menu.")
        print("Start Menu opened successfully!")
    except Exception as e:
        print(f"Error opening Start Menu: {e}")
        speak("Failed to open Start Menu.")

def close_chrome():
    try:
        pyautogui.hotkey("ctrl", "w")
        speak("Closing Chrome.")
        print("Chrome closed successfully!")
    except Exception as e:
        print(f"Error closing Chrome: {e}")
        speak("Failed to close Chrome.")

def close_terminal():
    try:
        print("Terminating Python process...")
        sys.exit()  # Ends the Python process
    except Exception as e:
        print(f"Error terminating terminal: {e}")
        speak("Failed to terminate Python process.")


def save_memory():
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file)


def process_command(command):
    # Hardcoded command checks for opening apps
    if "chrome" in command:
        open_chrome()
    elif "vscode" in command or "visual studio" in command:
        open_vscode()
    elif "github" in command:
        open_github_desktop()
    elif "explorer" in command or "file" in command:
        open_file_explorer()
    elif "start" in command:
        open_start_menu()

    # Hardcoded command checks for closing apps
    elif "close chrome" in command:
        close_chrome()

    # Close terminal command
    elif "end" in command:
        close_terminal()

    # Other command handling
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}.")
    elif "my name is" in command:
        name = command.split("my name is")[-1].strip().capitalize()
        memory["name"] = name
        save_memory()
        speak(f"Nice to meet you, {name}!")
    elif "what's my name" in command or "what is my name" in command:
        speak(f"Your name is {memory.get('name', 'unknown')}.")
    elif "my favorite color is" in command:
        color = command.split("my favorite color is")[-1].strip()
        memory["fav_color"] = color
        save_memory()
        speak(f"{color} is a lovely color!")
    elif "what's my favorite color" in command or "what is my favorite color" in command:
        speak(f"Your favorite color is {memory.get('fav_color', 'unknown')}.")
    else:
        speak("I’m not sure what you meant. Want me to look that up for you?")

def main():
    speak(get_time_based_greeting())
    speak(f"Hello {memory['name']}, I'm Xeno. What can I do for you?")

    while True:
        command = listen_to_command()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
