import os

import scipy as sp
from Back.speak import speak_only
import Back.editables
import webbrowser
# import app


def open_code():
    speak_only('Opening VS CODE')
    os.startfile(Back.editables.codePath)

def close_code():
    speak_only('Closing VS Code')
    os.system(f'taskkill /im code.exe /t /f')

def open_Blue():
    speak_only("Opning Bluestake")
    os.startfile(Back.editables.blue)

def close_Blue():
    speak_only('Closing Bluestake')
    os.system('taskkill /im HD-Player.exe /t /f')

def open_excel():
    speak_only("Opning Excel")
    os.startfile(Back.editables.excel)

def close_excel():
    speak_only('Closing Excel')
    os.system('taskkill /im EXCEL.exe /t /f')

def open_word():
    speak_only("Opning Word")
    os.startfile(Back.editables.word)

def close_word():
    speak_only('Closing Word')
    os.system('taskkill /im WINWORD.exe /t /f')

def open_explorer():
    speak_only('opening Explorer')
    os.startfile(Back.editables.explorer)

def close_explorer():
    speak_only('Closing Explorer')
    os.system('taskkill /im explorer.exe /t /f')

def open_zoom():
    speak_only('opening Zoom')
    os.startfile(Back.editables.zoom)

def close_zoom():
    speak_only('Closing Zoom')
    os.system('taskkill /im Zoom.exe /t /f')

def open_WhatsApp():
    speak_only("opening WhatsApp")
    os.system(Back.editables.WhatsApp) 

def close_WhatsApp():
    speak_only("closing WhatsApp")
    os.system('taskkill /im WhatsApp.exe /t /f')

def close_chrome():
    speak_only('Closing Chrome')
    os.system('taskkill /im chrome.exe /t /f')
    
def open_notepad():
    speak_only("opening notepad")
    os.system(Back.editables.notepad)

def close_pad():
    speak_only('Closing Notepad')
    os.system('taskkill /im notepad.exe /t /f')

def close_aternos():
    speak_only('closing Aternos')
    os.system('taskkill /im chrome.exe /t /f')

def open_moviesv():
    webbrowser.open("https://moviesverse.me/")
    speak_only("opening moviesveres") 

def open_M():
    os.system(Back.editables.g)

def close_M():
    # speak_only('closing Aternos')
    os.system('taskkill /im MPC-HC64.exe /t /f')