import pyautogui
import Back.editables
import datetime
from Back.speak import speak_only,speak
import os

def screenshot():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().strftime("%H-%M-%S")

    image = pyautogui.screenshot()
    image.save(Back.editables.screenshots + '/' + str(date) + '-' + str(time) + '.png')

    speak_only('Screenshot saved successfully')
    speak_only("And I Am Opeing screenshot folder")
    os.startfile('C:\\Users\\harsh\\OneDrive\\Pictures\\Screenshots')
