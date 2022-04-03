import Back.editables
from Back.speak import speak_only,speak
import Back.commands as cmd

def remember():
    speak_only('What should I remember?')
    answer = cmd.takeCommand().lower()
    file_name = Back.editables.remember + '/remember.txt'
    file = open(file_name, 'w')
    file.write(answer)
    speak_only('Okay, I\'ll remember it')
    file.close()


def read_remember():
    file_name = Back.editables.remember + '/remember.txt'
    file = open(file_name, 'r')
    speak(file.read())