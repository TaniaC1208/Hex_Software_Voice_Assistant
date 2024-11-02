import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

# Initialize the speech engine
engine = pyttsx3.init()

# Set properties for the voice (female voice)
voices = engine.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not request results from the service.")
            return None

def respond_to_command(command):
    """Respond to the user's command."""
    if 'what is your name' in command:
        speak("I am Poppaatlall, your personal voice assistant.")
    elif 'current time' in command:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%H:%M')}")
    elif 'date today' in command:
        now = datetime.datetime.now()
        speak(f"Today's date is {now.strftime('%B %d, %Y')}")
    elif 'wikipedia' in command:
        speak("What do you want to know about?")
        topic = listen()
        if topic:
            try:
                result = wikipedia.summary(topic, sentences=1)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple topics related to your request. Please be more specific.")
    elif 'stop' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I am sorry, I cannot help with that.")

# Main function to run the assistant
def main():
    speak("Hello, I am Poppaatlall. How can I assist you today?")
    while True:
        command = listen()
        if command:
            respond_to_command(command)

if __name__ == "__main__":
    main()
