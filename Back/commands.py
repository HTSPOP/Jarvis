from numpy import block
import speech_recognition as sr
from colorama import Fore, Style
from colored import attr
bold = attr(1)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print("         ")
        print(Fore.YELLOW + f"{bold}User Said : >>  {query}" + Style.RESET_ALL)

    except Exception as ex:
        print(ex)
        return 'None'

    return query

def takeCommand_without_print():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("         ")
        # print(Fore.YELLOW + f"{bold}Listening...." + Style.RESET_ALL)
        # print(Fore.YELLOW + 'Listening....' + Style.RESET_ALL)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # print("         ")
        # print(Fore.YELLOW + f"{bold}Recognizing...." + Style.RESET_ALL)
        # print(Fore.YELLOW + 'Recognizing....' + Style.RESET_ALL)
        query = r.recognize_google(audio, language='en-in')

    except Exception as ex:
        print("         ")
        print(ex)
        # print(Fore.YELLOW + f"{bold}Please tell again" + Style.RESET_ALL)
        # print(Fore.YELLOW + 'Please tell again' + Style.RESET_ALL)
        return 'None'

    return query
