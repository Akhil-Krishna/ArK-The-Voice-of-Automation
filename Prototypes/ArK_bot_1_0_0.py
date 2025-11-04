import speech_recognition as sr
import pyttsx3
from groq import Groq

#groq settings
groq_client = Groq(api_key="REDACTED")


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



def chat_with_llama(querry):
    try:
        
        user_message = querry
        prompt = "As a bot named Ark, please provide a breif and helpful answer to the following question:"+user_message

        # Call Groq API
        completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"You are Ark, a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",  # You can also use "llama2-70b-4096"
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            stream=False
        )
        
        response = completion.choices[0].message.content
        return response
            
            
    except Exception as e:
        print(e)
        return "Sorry I cant provide"
    
    
    
    

speak("How can I help you?")
while True:
    command = listen()
    
    resp = chat_with_llama(command)
    # if "```python" in resp:
    #     resp.replace('```','#')
    # elif "```" in resp:
    #     resp.replace('```','//')
    if "quit" in command:
        speak("Goodbye")
        break
    else:
        speak(resp)
