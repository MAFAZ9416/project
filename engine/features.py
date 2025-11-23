import os
from playsound import playsound
import eel
import pywhatkit as kit
import re
import sqlite3
import webbrowser
#import pygame

# Database connection
conn = sqlite3.connect('JAMAL.db')
cursor = conn.cursor()

from engine.command import speak
from engine.config import ASSISTANT_NAME

#sound function for playing sound
def playAssistantSound():
   music_dir = "C:\\Users\\mafaz\\Desktop\\project\\www\\assets\\audio\\start_sound.mp3" # thisd is the model of below function
   playsound(music_dir)


# def playAssistantSound():
#     pygame.mixer.init()
#     pygame.mixer.music.load("/home/mafaz/project/www/assets/audio/start_sound.mp3")
#     pygame.mixer.music.play()

#click sound for mic button

@eel.expose
def playClickSound():
    music_dir = "C:\\Users\\mafaz\\Desktop\\project\\www\\assets\\audio\\click_sound.mp3" # thisd is the model of below function
    playsound(music_dir)

# def playClickSound():
#     pygame.mixer.init()
#     pygame.mixer.music.load("/home/mafaz/project/www/assets/audio/click_sound.mp3")
#     pygame.mixer.music.play()
 

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip().lower()

    if query !="":
        try:
            # Try to find the application in sys_command table
            cursor.execute('SELECT path FROM LOCAL_PATH WHERE LOWER(name)= ?',(query,))
            results = cursor.fetchall()

            if len(results)!= 0:
                speak("Opening "+ query)
                os.startfile(results[0][0])
                return
        
            # If not found, try to find the URL in web_command table
            cursor.execute('SELECT ur1 FROM WEB_PATH WHERE LOWER(name)-?', (query,))
            results = cursor.fetchall()

            if len(results)!= 0:
                speak("Opening "+ query)
                webbrowser.open(results[0][0])
                return
            
            # IF still not found, try to open using os.system
            speak("Opening "+ query)
            try:
                os.system("start " + query)
            except Exception as e:
                speak(f"sorry,unable to open {query}.Error : {str(e)}")
                       
        except Exception as e:
            speak(f"somthing went wrong : {str(e)}")


def playyoutube(query):
    print(query)
    search_term = extract_yt_term(query)
    print(search_term)
    if search_term:
        speak("playing " + search_term + " on YouTube")
        kit.playonyt(search_term)

    else :
        speak("sorry, Could not find the search term for YouTube")

def extract_yt_term(command):
    print(command)
    pattern = r"play\s+(.*?)\s+(?:on\s+youtube|youtube)"
    print(pattern)
    match = re.search(pattern, command, re.IGNORECASE)
    print(match)
    return match.group(1) if match else None
    