import os
import eel
from engine.features import *
from engine.command import *
eel.init('www')

playAssistantSound()

os.system("start microsoft-edge:http://localhost:8000/index.html")
eel.start('index.html', mode='MicrosoftEdge', host='localhost', block=True)
