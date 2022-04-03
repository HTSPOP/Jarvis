import pyttsx3
from colorama import Fore, Style
import Back.editables
import pyttsx3
from colored import fg, attr

gold = fg(226)
orange = fg(202)
green = fg(46)
orange_4b = fg(94)

bold = attr(1)
reset = attr(0)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices.id)
engine.setProperty('voice', voices[ Back.editables.gender].id)


rate = engine.getProperty('rate')
engine.setProperty('rate',  Back.editables.rate)


def speak(audio):
    print("  ")
    print(f'{orange}{bold}Jarvis : {str(audio)}{reset}')
    engine.say(audio)
    engine.runAndWait()


def speak_only(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("hallow")
# import Back.editables
#         import Back.speak 
#         import Back.commands as cmd
#         time.sleep(2)
#         name = Back.editables.UserName
#         real_name = Back.editables.real_name
#         real_password = Back.editables.Password
#         notLogged = True
#         password_count = 0
#         Back.speak.speak('Hello, Please tell me the password?')
#         while notLogged:
#             password_count = password_count + 1
#             password = cmd.takeCommand().lower()
#             # password = input("\nEnter Password : ")

#             if password == real_password:
#                 notLogged = False
#                 speak_only("OK Password Is correct")
#                 jarvis()
#             elif password_count >= 5:
#                 Back.speak.speak('Going offline')
#                 break
#             elif password == 'none':
#                 Back.speak.speak('Please tell me the password?')
#             elif 'bye bye' in password:
#                 Back.speak.speak('Going offline')
#                 break
#             elif 'go offline' in password:
#                 Back.speak.speak('Going offline')
#                 break
#             else:
#                 Back.speak.speak('Wrong Password, Please try again....')