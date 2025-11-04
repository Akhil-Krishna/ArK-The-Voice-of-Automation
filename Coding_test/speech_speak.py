import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
    engine.setProperty('rate', 170)  # Speed of speech
    engine.setProperty('volume', 1.0)
    print("ArK : ",text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold=1.5
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"You : {command}")
    except:
        command = ""
        speak("Sorry, I didn't catch that.")
    return command.lower()



speak("How can I help you?")
while True:
    command = listen()

    if 'hello' in command:
        resp = "Hello Akhil, nice to talk to you."
        speak(resp)
    elif 'your name' in command:
        resp = "I am ArK, your personal AI assistant."
        speak(resp)
    elif 'stop' in command or 'exit' in command:
        resp = "Good Byeee"
        speak("Goodbye!")
        break
