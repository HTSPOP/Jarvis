from Back.speak import speak_only
import datetime as dt
import Back.commands as cmd
from colorama import Fore, Style
import os


# Time
def tell_time():
    time = dt.datetime.now().strftime("%H:%M:%S")
    speak_only(Fore.GREEN + dt.datetime.now().strftime("%H:%M:%S") + Style.RESET_ALL)
    print("                    ")
    speak_only(time)

# Date
def tell_date():
    date = dt.datetime.now().date()
    print("                    ")
    speak_only(date)

# Shutdown Computer
def shutdown():
    speak_only('Do you want to shutdown your computer?')
    answer = cmd.takeCommand().lower()

    if 'yes' in answer or 'sure' in answer:
        speak_only('Shutting down computer!')
        os.system("shutdown /s /t 1")


# Restart Computer
def restart():
    speak_only('Do you want to restart your computer?')
    answer = cmd.takeCommand().lower()

    if 'yes' in answer or 'sure' in answer:
        speak_only('Restarting computer!')
        os.system("shutdown /r /t 1")


def logout():
    speak_only("Loging out.....")
    os.system("shutdown -1")