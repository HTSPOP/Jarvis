from fileinput import filename
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
from Back.speak import speak_only
import datetime
from Back.commands import takeCommand

def notepad():
    speak_only('Tell Me The Query .')
    speak_only("I Am Ready To Write")
    writes = takeCommand()
    time = datetime.datetime.now().strftime("%H:%M")
    fileName = str(time).replace(':',"-") + "-Note.txt"
    with open(fileName,'w') as file:
        file.write(writes)
    path_1 ="P:\\jarvis-main\\" + str(fileName)
    path_2 ='P:\\jarvis-main\\Note\\'+ str(fileName)
    import os
    os.rename(path_1,path_2)
    os.startfile(path_2)
def CloseNotePad():
    import os
    os.startfile("TASKKILL /F /im Notepad.exe")