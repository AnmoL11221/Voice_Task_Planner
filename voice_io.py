import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    print(f"🤖 AI: {text}")
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen_for_command() -> str:
    """Captures microphone input and converts it to text."""
    with sr.Microphone() as source:
        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("👂 Transcribing...")
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"❌ Could not request results from Google Speech Recognition service; {e}")
        return None