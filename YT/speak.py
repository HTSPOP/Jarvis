import pyttsx3
from colorama import Fore, Style

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', '200')


def speak(audio):
    print(Fore.GREEN + str(audio) + Style.RESET_ALL)
    engine.say(audio)
    engine.runAndWait()


def speak_only(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("hallow I AM PRO AND PRO")