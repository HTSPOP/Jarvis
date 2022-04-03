
import datetime
import PyPDF2
import psutil
from notifypy import Notify
from colorama import Fore, Style
import socket
import sys
import requests
import bs4
import geocoder
import json
# import Back.commands as cmd
import speech_recognition as sr
from Back.speak import speak
from colored import fg, attr

# if __name__ == "__main__" :
#     run()
bold = attr(1)
reset = attr(0)
gold = fg(226)
orange = fg(202)
green = fg(46)
orange_4b = fg(94)

def weather():
    try: 
        from Back.speak import speak_only,speak
        g = geocoder.ip('me')
        data = json.load(open('data.json'))
        api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
            str(g.latlng[0]) + "&lon=" + str(g.latlng[1])
        data = requests.get(api_url)
        data_json = data.json()
        if data_json['cod'] == 200:
            main = data_json['main']
            wind = data_json['wind']
            weather_desc = data_json['weather'][0]
            speak('Sir Our latitude Is ' +str(data_json['coord']['lat']) + ' And our longitude Is ' + str(data_json['coord']['lon']))
            speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
            speak('weather type ' + weather_desc['main'])
            speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
            speak('Temperature: ' + str(main['temp']) + ' degree celcius')
            speak('Humidity is ' + str(main['humidity']))
    except:
        speak("You Are Not Connected To Internet That's Why I can't Give Weather Report")

def weather2():
    from Back.speak import speak_only,speak
    g = geocoder.ip('me')
    data = json.load(open('data.json'))
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('weather type ' + weather_desc['main'])
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Temperature: ' + str(main['temp']) + ' degree celcius')
        speak('Humidity is ' + str(main['humidity']))

def Location():
    g = geocoder.ip('me')
    data = json.load(open('data.json'))
    from Back.speak import speak_only,speak
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        print("")
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        print("")

def wish():
    import time
    from Back.speak import speak_only,speak
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%p")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        time.sleep(1)
        speak(f"Good morning sir and Its : {current_time}")
        print(" ")
    elif hour >= 12 and hour < 18:
        time.sleep(1)
        speak(f"Good afternoon Sir and Its : {current_time}")
        print(" ")
    else:
        time.sleep(1)
        speak(f"Good evening sir and Its : {current_time}")

def help():
    import time
    from Back.speak import speak_only
    time.sleep(2)
    speak_only("Sir Read All Commands and Then")
    mute()

def pdf_reader():
    from Back.speak import speak_only,speak

    print("    ")
    speak_only("Enter The Path Of PDF ")
    print("    ")
    path = input("Enter The Path Of Pdf: ")
    book = open(path, "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak_only(f"Total Numbers of pages in this book are : {pages}")
    print(f"Total Numbers of pages in this book are : {pages}")
    speak_only("Sir Please enter the page number i have to read")
    print("    ")
    pg = int(input("Please Enter The Page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    print(text)
    speak(text)

def wait():
    import time
    print(Fore.GREEN + f"{bold}\nWaiting ", end="" + Style.RESET_ALL)
    list1 = [Fore.GREEN + f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.",f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.", f"{bold}.",'\n'+ Style.RESET_ALL]
    for i in (list1):
        print(f"{i}", end="")
        time.sleep(1)

def cpu():
    from Back.speak import speak_only,speak
    usage = str(psutil.cpu_percent())
    speak("Sir System CPU is at " + usage)

def memory():
    from Back.speak import speak_only,speak

    mem = str(psutil.virtual_memory())
    mem = mem.split(",")
    i = mem[2].split("=")
    speak("Sir System Memory Percentage is " + i[1] + "%")
    j = mem[1].split("=")
    speak("Sir System Free Memory is at " + j[1])

def battery():
    from Back.speak import speak_only,speak

    batt = str(psutil.sensors_battery())
    batt = batt.split()
    i = batt[0].split("(")
    i = i[1].split("=")
    speak("Sir System battery is at " + i[1] + "%")

def TimeTable():
    from Back.speak import speak_only,speak
    from time import sleep
    speak_only("Now , Checking The Time Table..........")
    from Back.timetable import time

    value = time()
    Noti = Notify()
    Noti.title = "TimeTable"
    Noti.message = str(value)
    Noti.icon = "G:\\Jarvis 1 (With GUI)\\Back\\i.png"
    Noti.send()
    import Back.bd

    speak_only("AnyThing Else Sir ")
    sleep(1)
    print(" ")

    print(
        Fore.BLUE + f"{bold}Sir ,IF You What TO know My commands Say [Help Me Jarvis] " + Style.RESET_ALL
    )

def Noti():
    Noti1 = Notify()
    Noti1.title = "Jarvis Activated By Harsh"
    Noti1.message = str("Jarvis Is Not Activated")
    Noti1.icon = "j.png"
    Noti1.send()

def Temp():
    from Back.speak import speak_only,speak
    g = geocoder.ip('me')
    data = json.load(open('data.json'))
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        print (' ')
        speak('Temperature: ' + str(main['temp']) + ' degree celcius')

def check_internet():
    try:
        from Back.speak import speak_only,speak

        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        speak_only(
            "Please Wait Sir .... I am checking your internet connection..."
        )
        wait()
        speak_only("Your Internet is Working Sir")
    except Exception as e:
        speak_only(
            "Please Wait Sir .... \nI am checking your internet connection..."
        )
        wait()
        speak_only(
            "Your Internet connection is down Sir...But i am still Checking....\n"
        )
        sys.exit()

def CoronaVirus(Country):
    import lxml
    from Back.speak import speak_only,speak
    Counteries = str(Country).replace(" ", "")
    url = f"https://www.worldometers.info/coronavirus/country/{Counteries}/"
    result = requests.get(url)
    soups = bs4.BeautifulSoup(result.text, "lxml")
    corona = soups.find_all("div", class_="maincounter-number")
    Data = []
    for case in corona:
        span = case.find("span")
        Data.append(span.string)
    cases, Death, reco = Data
    print("   ")
    speak(f"COVID CASES : {cases}")
    print("   ")
    speak(f"COVID DEATHS : {Death}")
    print("   ")
    speak(f"COVID RECOVERED : {reco}")

def Finish():
    print('Done Download!')

def Notif():
        noti = Notify()
        noti.title = 'Jarvis'
        noti.message = 'Jarvis Is Activated'
        noti.icon = 'j.png'
        noti.send()

def T():
    import time
    from Back.speak import speak_only,speak
    import random
    wi = [5,10,15,20,25,30,35,40,45,50,55,60]
    wi1 = random.choice(wi)
    speak(f"\nSir Wait I Am Cheaking The System Please Wait {wi1} Seconds ")
    time.sleep(wi1)
    speak(f"\nAll done Sir I Have Cheak The System in {wi1} Seconds ")
    time.sleep(2)

def mute():

    global listen
    listen = False
    # speak("Listening stopped.")
    # print(f"{gold}{bold}Listening stopped. {reset}")
    speak("Say jarvis to listen")
    r = sr.Recognizer()
    while listen is False:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  # Eliminating the noise.
            r.pause_threshold = 1
            audio = r.listen(source, timeout=20, phrase_time_limit=10)
        try:
            query = r.recognize_google(audio).lower()  # Converting speech to text
            if query == "jarvis":
                listen = True
                speak("Voice mode activated")
                break
            else:
                continue
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Uh oh! Sorry sir Couldn't understand my brains not feeling so good can't get a connection.")
        except KeyboardInterrupt:
            pass
    return listen

def Alarm(query):
    import os
    TIMEHeare = open("B:\\Jarvis 4 (Without GUI)\\Back\\Data.txt",'a')
    TIMEHeare.write(query)
    TIMEHeare.close()
    os.startfile("B:\\Jarvis 4 (Without GUI)\\Back\\Alarm.py")

Alarm('set alarm for 19 and 6')