import speech_recognition as sr

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1.5
        audio = r.listen(source,timeout=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"You said: {query}")
    except Exception as e:
        print("Sorry, I couldn't understand.")
        
    if "quit" in query:
        break