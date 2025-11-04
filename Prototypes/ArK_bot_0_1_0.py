import speech_recognition as sr
import pyttsx3
import os
import pyautogui as py
import time

def speak(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()
    
def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        
        #background noise removal
        recognizer.adjust_for_ambient_noise(source,duration=1)
        
        #pausing before action
        recognizer.pause_threshold=1.5
        
        #extract audio
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
    except:
        text = "Sorry Cant help"
        
    return text

def write_text(text):
    os.system("notepad")
    time.sleep(1)
    py.typewrite(text,interval=0.26)
    time.sleep(1)
    file_name = py.prompt("File name : ",default='Ark')
    py.hotkey('ctrl','s')
    time.sleep(1)
    py.typewrite(f"{file_name}.txt")
    
def write_code(code):
    time.sleep(3)
    py.hotkey('ctrl','n')
    time.sleep(1)
    py.typewrite(code)
    file_name = py.prompt("File name : ",default="ark")
    py.hotkey('ctrl','s')
    time.sleep(1)
    py.typewrite(f"{file_name}.py")
    
    
    

def open_(app):
    os.system(f"{app}")
    
    

def main():
    while True:
        query = listen().lower()
    
        if "stop" in query:
            break
        
        if "open" in query:
            if "notepad" in query:
                text = query.split("write")[1]
                write_text(text)
            elif "vscode" in query:
                #open("code")
                write_code("print('haiiiii')")
            
    
        speak(query)
    
    
if __name__ =="__main__":
    main()
    
    
        
        
        