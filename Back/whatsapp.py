from numpy import rec
import pywhatkit as whatsApp
from Back.phone_book import contacts
import speak
import commands
import datetime as dt


def sendwhatsapp():
    speak.speak_only('\n To whom?')
    receiver = commands.takeCommand()    
    # receiver = input()
    receiver = receiver.lower()

    try:
        receiver_number = contacts[receiver]
        speak.speak_only('\n What should I send?\n')
        # msg = input()
        msg1 = "Hallo I Am Jarvis AI By Harsh . Harsh Tell ME TO send This Message :- " + msg
        msg = commands.takeCommand()        
        hours = int(dt.datetime.now().strftime("%H"))
        min = int(dt.datetime.now().strftime("%M"))
        sec = int(dt.datetime.now().strftime("%S"))

        if sec < 30:
            min = min + 1

            if min == 60:
                hours = hours + 1
                min = 00

                if hours == 24:
                    hours = 00

        else:
            min = min + 2
            if min > 59:
                hours = hours + 1
                min = 00

                if hours == 24:
                    hours = 00

        whatsApp.sendwhatmsg(receiver_number,msg1,hours, min, 20, True, True)
        # whatsApp.sendwhatmsg(receiver_number,msg, hours, min, 20, True, True)
        # whatsApp.sendwhatmsg(receiver_number,msg,min,20,True,True)
        speak.speak_only(f' Message Delivered to {receiver}')

    except KeyError:
        speak.speak_only('Can\'t find that contact')
# sendwhatsapp()