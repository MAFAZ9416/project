import os
from playsound import playsound
import eel
import pywhatkit as kit
import re
#import pygame

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
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("Opening " + query)
        os.system('start ' + query)

    # elif query != "":
    #     speak("closing" + query)
    #     os.system('taskkill /im ' + query + '.exe /f')

    else:
        speak(f"{query} not found") 

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
    