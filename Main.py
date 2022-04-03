from ast import operator
import instaloader
import pyttsx3
import speech_recognition as sr
import time
import wikipedia
from colorama import Fore, Style
from keyboard import press_and_release
from colorama import Fore, Style
import Back.editables
from Back.speak import speak_only
from Back.speak import speak
from Back.Features import Notif

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[Back.editables.gender].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', Back.editables.rate)
Notif()

def run():
        import Back.editables
        import Back.speak 
        import Back.commands as cmd
        time.sleep(2)
        name = Back.editables.UserName
        real_name = Back.editables.real_name
        real_password = Back.editables.Password
        notLogged = True
        password_count = 0
        count = 5
        count2 = 5
        Back.speak.speak('Hello, Please tell me the password?')
        while notLogged:
            password_count = password_count + 1
            password = cmd.takeCommand().lower()
            # password = input("\nEnter Password : ")

            if password == real_password:
                notLogged = False
                speak_only("OK Password Is correct")
                jarvis()
            elif password_count >= 5:
                Back.speak.speak('Going offline')
                break
            elif password == 'none':
                count2 = count + 1 
                Back.speak.speak(f'Please tell me the password?')
            elif 'bye bye' in password:
                Back.speak.speak('Going offline')
                break
            elif 'go offline' in password:
                Back.speak.speak('Going offline')
                break
            else:
                count2 = count + 1 
                Back.speak.speak(f'Wrong Password, Please try again....')

def STT():
        from colored import fg, attr
        bold = attr(1)
        from Back.speak import speak,speak_only
        R = sr.Recognizer()

        with sr.Microphone() as source:
            audio = R.listen(source)

        try:
            text = R.recognize_google(audio, language="en-in")
            print("                    ")
            print(Fore.YELLOW + f"{bold}User Said : >>  {text}" + Style.RESET_ALL)

        except Exception:
            return "None"
        text = text.lower()
        return text

def jarvis():

        import time

        from Back.Features import wish,weather,TimeTable

        from Back.speak import speak_only,speak

        import webbrowser

        import pyautogui

        import random
 
        from Back.Features import wait

        wi1 = [5,10,15,20,25,30,35,40,45,50,55,60]
 
        wi2 = random.choice(wi1)
 
        speak(f"Sir Wait I Am Checking The System Till There You See Youtube Ok ")
 
        webbrowser.open("https://www.youtube.com")
 
        time.sleep(wi2)
 
        pyautogui.press('Space')
 
        speak(f"All done Sir I Have Checked The System in {wi2} Seconds")
 
        time.sleep(2)
 
        wish()
 
        weather()
 
        TimeTable()

        while True:
            query = STT()

# PC

            if "pc" in query:
                from Back.Features import cpu,memory,battery

                cpu()
                memory()
                battery()

            elif "internet speed" in query:
                from Back.speed import SpeedTest
                SpeedTest()

            elif "shutdown" in query:
                from Back.basic import shutdown
                shutdown()

            elif "log out" in query:
                import os

                speak_only("Sir system is logging out")
                speak_only("Sir Goodbye")
                os.system("shutdown -l")

            elif "reboot" in query:
                from Back.basic import restart
                restart()

            elif "no voice" in query or 'sleep' in query:
                from Back.Features import mute
                mute()

            elif "wikipedia" in query:
                from Back.speak import speak_only,speak

                speak_only("searching details....Wait")
                query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print("                    ")
                speak(results)

            elif "date" in query:
                from Back.basic import tell_date
                tell_date()

            elif "time" in query:
                import datetime
                ct = datetime.datetime.now().strftime("%I:%M:%p")
                speak(f"\nThe Current Time Is = {ct}")

            elif "day" in query:
                from Back.speak import speak_only,speak
                from datetime import datetime

                print("                    ")

                speak(f"Sir , Today is {datetime.today().strftime('%A')}")

            elif "set alarm" in query:
                from Back.speak import speak_only,speak 
                from Back.Myalarm import alarm

                speak_only("\nPlease Enter The Time : ")
                tt = input("\nPlease Enter The Time : ")
                tt = tt.upper()
                import Back.Myalarm

                alarm(tt)

            elif "temperature" in query:
                from Back.Features import Temp

                Temp()

            elif "check internet" in query:
                from Back.Features import check_internet
                check_internet()

            elif 'birthday' in query:
                from Back import bd
                bd()

# softwere-start

            elif "open vs code" in query:
                from Back.application import open_code

                open_code()

            elif "open blue" in query:
                from Back.application import open_Blue

                open_Blue()

            elif "open excel" in query:
                from Back.application import open_excel   
                
                open_excel()

            elif "open word" in query:
                from Back.application import open_word

                open_word()

            elif "open explorer" in query:
                from Back.application import open_explorer

                open_explorer()

            elif "open zoom" in query:
                from Back.application import open_zoom

                open_zoom()

            elif "open whatsapp" in query:
                from Back.application import open_WhatsApp

                open_WhatsApp()

# Software - Close

            elif "close vs code" in query:
                from Back.application import close_code

                close_code()

            elif "close blue" in query:
                from Back.application import close_Blue

                close_Blue()

            elif "close zoom" in query:
                from Back.application import close_zoom

                close_zoom()

            elif "close word" in query:
                from Back.application import close_word

                close_word()

            elif "close excel" in query:
                from Back.application import close_excel

                close_excel()

            elif "close whatsapp" in query:
                from Back.application import close_WhatsApp

                close_WhatsApp()

# Folder Can't Close Black Screen

            elif "open movie folder" in query:
                import os
                from Back.speak import speak_only
                from Back.speak import speak
                speak_only("opening MOVIES AND WEB")
                movies1 = "B:\\"
                os.startfile(movies1)

            elif "open python folder" in query:
                import os
                from Back.speak import speak_only
                from Back.speak import speak
                speak_only("opening Python Folder")
                python = "F:\\"
                os.startfile(python)

            elif "delete movie" in query:
                import os
                from Back.speak import speak_only
                from Back.speak import speak
                location = "B:\\"
                video = os.listdir(location)
                print("    ")
                print(f"This Are The Files In The Movies Folder : \n{video}")
                speak_only(f"This Are The Files In The Movies Folder : {video}")
                speak_only("Please Enter The Name Of File")
                print("    ")
                file = input("Please Enter The Name Of File : ")
                try:
                    path = os.path.join(location, file)
                    os.remove(path)
                    speak_only("Deteted Successfully........")
                except:
                    speak_only("Movie not Founded In Movies Folder")

# rem and Volume

            elif "what do you remember" in query:
                from Back.rem import read_remember
                read_remember()

            elif "remember" in query:
                from Back.rem import remember
                remember()

            elif "read pdf" in query:
                from Back.Features import pdf_reader
                
                pdf_reader()

            elif "volume up" in query:
                from Back.v import Volume_Up

                Volume_Up()

            elif "volume down" in query:
                from Back.v import volume_down

                volume_down()

            elif "mute" in query:
                from Back.v import volume_mute

                volume_mute()

# Browser - open

            elif "new tab" in query:
                from Back.speak import speak_only
                speak_only("OK")
                press_and_release("ctrl + t")

            elif "new window" in query:
                from Back.speak import speak_only
                speak_only("OK")
                press_and_release("ctrl + n")

            elif "history" in query:
                from Back.speak import speak_only
                speak_only('ok')
                press_and_release("ctrl + h")

            elif "chrome download" in query:
                from Back.speak import speak_only
                speak_only("OK")
                press_and_release("ctrl + j")

            elif "open youtube" in query or "open video online" in query:
                import webbrowser
                from Back.speak import speak_only
                speak_only("Opening Youtube")
                webbrowser.open("https://www.youtube.com")

            elif "open facebook" in query:
                import webbrowser
                from Back.speak import speak_only
                webbrowser.open("https://www.facebook.com")
                speak_only("opening facebook")

            elif "open instagram" in query:
                import webbrowser
                from Back.speak import speak_only
                webbrowser.open("https://www.instagram.com")
                speak_only("opening instagram")

            elif "open google" in query or "open chrome" in query:
                import webbrowser
                from Back.speak import speak_only
                webbrowser.open("https://www.google.com")
                speak_only("opening google")

            elif "open yahoo" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://www.yahoo.com")
                speak_only("opening yahoo")

            elif "open downloader" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open(
                    "https://loader.to/en68/youtube-downloader-chrome-extension.html"
                )
                speak_only("opening Yt downloader")

            elif "open wi-fi" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("http://192.168.0.1/")
                speak_only("opening WIFI Settings")

            elif "open gmail" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://mail.google.com")
                speak_only("opening google mail")

            elif "open speed test" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://www.speedtest.net/")
                speak("opening Speedtest website")

            elif "open snapdeal" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://www.snapdeal.com")
                speak_only("opening snapdeal")

            elif "open amazon" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")

            elif "open minecraft server" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://aternos.org/servers/")
                speak_only("Opening Aternos Website")

            elif "open flipkart" in query:
                import webbrowser
                from Back.speak import speak_only

                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")

            elif "search in youtube" in query:
                from Back.speak import speak_only
                from Back.commands import takeCommand
                from colorama import Fore, Style
                import webbrowser

                speak_only("sir What Do You Whant to search in Youtube")
                print("    ")
                ttt = takeCommand()
                query = ttt.lower()
                print("    ")
                print(
                    Fore.LIGHTYELLOW_EX
                    + "Opening Google and search about "
                    + Fore.LIGHTBLUE_EX
                    + query
                    + Style.RESET_ALL
                )
                speak_only(f"Opening YouTube and search about {query}")
                webbrowser.open("https://www.youtube.com/results?search_query=" + query)

            elif "search in google" in query:
                from Back.speak import speak_only
                from colorama import Fore, Style
                import webbrowser

                speak_only("sir What Do You Whant to search in Google")
                print("    ")
                ttt5 = takeCommand()
                query = ttt5.lower()
                print("    ")
                print(
                    Fore.LIGHTYELLOW_EX
                    + "Opening Google and search about "
                    + Fore.LIGHTBLUE_EX
                    + query
                    + Style.RESET_ALL
                )
                speak_only(f"Opening google and search about {query}")
                webbrowser.open("https://www.google.com/search?q=" + query)

# Browser :- close

            elif "close tab" in query:
                press_and_release("ctrl + w")

            elif "close youtube" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing Youtube")
                Back.application.close_chrome()

            elif "close minecraft server" in query:
                import Back.application
                from Back.speak import speak_only


                Back.application.close_aternos()

            elif "close flipkart" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing flipkart")
                Back.application.close_chrome()

            elif "close amazon" in query:
                speak_only("Closing amazom")
                import Back.application
                from Back.speak import speak_only


                Back.application.close_chrome()

            elif "close snapdeal" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing snapdeal")
                Back.application.close_chrome()

            elif "close gmail" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing gmail")
                Back.application.close_chrome()

            elif "close wi-fi" in query:
                import Back.application
                from Back.speak import speak_only


                Back.application.close_chrome()
                speak_only("Closing Wifi")

            elif "close downloader" in query:
                import Back.application
                from Back.speak import speak_only


                Back.application.close_chrome()
                speak_only("closing Yt downloader")

            elif "close yahoo" in query:
                import Back.application
                from Back.speak import speak_only


                Back.application.close_chrome()
                speak_only("Closing Yahoo")

            elif "close facebook" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing Facebook")
                Back.application.close_chrome()

            elif "close google" in query or "close chrome" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing Google")
                Back.application.close_chrome()

            elif "close instagram" in query:
                import Back.application
                from Back.speak import speak_only


                speak_only("Closing Instgram")
                Back.application.close_chrome()

# Videos and music

            elif "play music" in query or "play song" in query:

                import playsound
                import Back.speak
                from colorama import Fore, Style
                import time
                from Back.commands import takeCommand
 
                speak_only("Please Enter Song Number ")
                print("    ")
                print(
                    Fore.CYAN
                    + "There Are 33 Songs and song start from 1 and If You Whant To Play All Song write All"
                    + Style.RESET_ALL
                )
                while True:
                    ans = takeCommand()
                    try:
                        if "1" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\01.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "2" in ans or "tu" in ans or "do" in ans:                    
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\02.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "3" in ans or "third" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\03.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "4" in ans or "fourth" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\Music\\04.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "5" in ans or "fifth" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\05.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "6" in ans or "sixth" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\06.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "7" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\07.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "8" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\08.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "9" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music0\\9.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "10" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\10.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "11" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\11.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "12" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\12.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "13" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\13.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "14" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\14.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "15" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\15.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "16" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\16.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "17" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\17.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "18" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\18.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "19" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\19.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "20" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\20.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "21" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\21.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "23" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\22.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "24" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\23.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "25" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\24.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "26" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\25.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "27" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\26.wav")
                            speak_only("Yes Harsh I Am Back")
                            break

                        elif "28" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\27.wav")
                            speak_only("Yes Harsh I Am Back")

                        elif "29" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\28.wav")
                            speak_only("Yes Harsh I Am Back")

                        elif "30" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\30.wav")
                            speak_only("Yes Harsh I Am Back")

                        elif "31" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\31.wav")
                            speak_only("Yes Harsh I Am Back")

                        elif "32" in ans:
                            speak_only("Ok Please Wait For 2 second")
                            time.sleep(2)                    
                            playsound.playsound("G:\\Jarvis 4 (Without GUI)\\Music\\32.wav")
                        
                        elif 'random' in ans:
                            s = [
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\01.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\02.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\03.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\04.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\05.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\06.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\07.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\08.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\09.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\10.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\11.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\12.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\13.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\14.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\15.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\16.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\17.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\18.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\19.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\20.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\21.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\22.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\23.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\24.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\25.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\26.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\27.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\28.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\29.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\30.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\31.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\32.wav",
                                    ]
                            import random
                            r = random.choice(s)

                        elif "all" in ans or "All" in ans:
                            from colorama import Fore, Style

                            speak_only(
                                "Sir You Really Whant Do Play All Music |  If You Whant To Break You Have To Stop Terminal Ok | IF You Whant To Prossed Type Yes Else No "
                            )
                            print("    ")
                            print(
                                Fore.RED
                                + "Warning : Sir You Really Whant Do Play All Music |  If You Whant To Break You Have To Stop Terminal Ok | IF You Whant To Prossed Type Yes Else No"
                                + Style.RESET_ALL
                            )
                            print("    ")
                            y = takeCommand()

                            if "yes" in y or "Yes" in y or "y" in y or "Y" in y:
                                speak_only("OK SIR I AM Playing Music")
                                while True:
                                    s = [
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\01.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\02.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\03.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\04.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\05.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\06.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\07.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\08.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\09.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\10.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\11.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\12.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\13.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\14.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\15.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\16.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\17.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\18.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\19.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\20.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\21.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\22.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\23.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\24.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\25.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\26.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\27.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\28.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\29.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\30.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\31.wav",
                                    "G:\\Jarvis 4 (Without GUI)\\Music\\32.wav",
                                    ]
                                    s1 = random.choice(s)
                                    print("    ")
                                    print("I Am Playing :", s1)
                                    print("    ")
                                    playsound.playsound(s1)
                                    time.sleep(2)

                    except:
                        "Music Not Found"

            elif "play video" in query:

                import os
                from Back.speak import speak_only

                video_dir = "B:\\"
                videos = os.listdir(video_dir)
                print("           ")
                print("In This Folder This are The Movies : ", videos)
                speak_only("In This Folder This are The Movies : ")
                speak_only(videos)
                print("           ")
                import time

                time.sleep(2)
                speak_only(
                    "Sir Please Enter The Number OF Movie Whic I Have To Play Also: "
                )
                print("           ")
                print("Note : countting Start From Zero")
                print("           ")

                vv = int(
                    input("Sir Please Enter The Number OF Movie Whic I Have To Play : ")
                )

                try:
                    print("  ")
                    speak("ok i am playing videos")
                    os.startfile(os.path.join(video_dir, videos[vv]))

                except:
                    speak_only("Sir I Not Fund The Video")

            elif "Stop" in query or "resume" in query:
                import pyautogui
                pyautogui.press("Space")

# jarvis commands

            elif "how are you" in query:
                stMsgs = [
                    "I am fine ! Sir , How are you",
                    "Nice ! sir",
                    "I am nice and full of energy",
                    "i am okey ! How are you",
                ]
                ans_q = random.choice(stMsgs)
                speak_only(ans_q)

            elif "fine" in query or "happy" in query or "ok" in query:
                speak_only("okey..")

            elif "make you" in query or "created you" in query or "develop you" in query:
                ans_m = " For your information Harsh Telavane make ! I give Lot of Thanks to Him "
                speak_only(ans_m)

            elif "who are you" in query or "about you" in query or "your details" in query:
                about = "I am  an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                speak_only(about)

            elif "switch the window" in query:

                import pyautogui
                import time

                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "hello" in query or "hello Jarvis" in query:
                hel = "Hello Harsh ! How May i Help you.."
                speak_only(hel)

            elif "your name" in query or "sweat name" in query:
                na_me = "Thanks for Asking my name my self ! Jarvis"
                speak_only(na_me)

            elif "how you feel" in query:
                speak_only("feeling Very sweet after meeting with you")

            elif "screenshot" in query:
                from Back.screenshot import screenshot
                screenshot()

            elif "help me jarvis" in query:
                import os
                from Back.Features import help

                os.startfile(
                    "G:\\Jarvis 4 (Without GUI)\\command.txt"
                )
                help()

# AUTO

            elif "write a note" in query:
                from Back.automa import notepad

                notepad()

# CORONA

            elif "corona" in query or "covid" in query:
                from Back.Features import CoronaVirus
                from Back.commands import takeCommand
                speak_only("PLease Tell Me Country Name")
                print("   ")
                Con = takeCommand()
                print("   ")
                CoronaVirus(Con)

# Instagram
  
            elif 'instagram profile' in query:
                speak_only("Sir Please Enter The User Name Corrctly.")
                name= input("Enter UserName Here : ")
                webbrowser.open(f'www.instagram.com/{name}')
                speak_only(f"Sir Here Is the profile of the User {name}")
                time.sleep(5)
                speak_only("Sor Wold you like to download profile pictyre of this account.")
                condi = takeCommand().lower()

                if 'yes' in condi:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak_only('I am done ,profile is saved in our main folder.now i am ready for next command')

                else :
                    pass

# Cal

            elif 'can you calculate' in query or 'do some calculation' in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("   ")
                    speak(" Say What you whant to calulate , for example : 3 plus 3 ")
                    print(Fore.YELLOW + "Listening...." + Style.RESET_ALL)
                    
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                    }[op]
                def eval_binary_expr(op1,oper,op2):
                    op1,op2 = int(op1),int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak_only('Your result is')
                speak(eval_binary_expr(*(my_string.split())))

# Phonenumbers

            elif 'phonenumber' in query:
                import phonenumbers
                from phonenumbers import geocoder
                from phonenumbers import carrier
                from phonenumbers import timezone
                from Back.speak import speak_only

                speak_only("Please Tell ME Number Down")
                number = input('\nEnter Number Here : ')

                ch_number = phonenumbers.parse(number,'CH')
                number_count = geocoder.description_for_number(ch_number,'en')
                servic = phonenumbers.parse(number,'RO')
                number_S = carrier.name_for_number(servic,'en')
                phone_num = phonenumbers.parse(number)
                time_zon = timezone.time_zones_for_number(phone_num)

                speak(f"\nCountry : {number_count}")
                speak(f"\nTimezone : {time_zon}")
                speak(f"\nService/Carrier Provider : {number_S}")

# Whatspp
 
            elif 'whatsapp' in query:
                from Back.whatsapp import sendwhatsapp
                sendwhatsapp()

# Find Location

            elif 'where is' in query:
                from Back.Mylocation import GoogleMaps
                place = query.replace('where is','')
                place = place.replace('jarvis','')
                GoogleMaps(place)

# Youtube Videos and delete
 
            elif "play youtube video" in query:
                import os
                import Back.speak

                video_dir = "Y:\\"
                videos = os.listdir(video_dir)
                print("           ")
                print("In This Folder This are The Movies : ", videos)
                speak_only("In This Folder This are The Movies : ")
                speak_only(videos)
                print("           ")
                import time

                time.sleep(2)
                speak_only(
                    "Sir Please Enter The Number OF Movie Whic I Have To Play Also: "
                )
                print("           ")
                print("Note : countting Start From Zero")
                print("           ")

            elif "delete movie" in query:
                import os

                location = "D:\\"
                video = os.listdir(location)
                print("    ")
                print(f"This Are The Files In The Youtube Video Folder : {video}")
                speak_only(f"This Are The Files In The Youtube Video Folder : {video}")
                speak_only("Please Enter The Name Of File")
                print("    ")
                file = input("Please Enter The Name Of File : ")
 
                try:
                    path = os.path.join(location, file)
                    os.remove(path)
                    speak_only("Deteted Successfully........")

                except:
                    speak_only("Youtube Video not Founded In Movies Folder")

# Hide File

            elif 'hide all file' in query or 'hide this folder' in query or 'visible for everyone' in query:
                speak_only('Sir Please Tell me you want to hide this folder or make it visible for everyone')
                con = takeCommand().lower

                if "hide" in con:
                    speak_only("Plase Enter The Path ")
                    Path = input("Enter The Path : ")
                    os.system("attrib +h " + Path)
                    speak_only("Sir , All The Files in This Folder Are now Hidden.")

                elif 'visible' in con:
                    speak_only("Plase Enter The Path ")
                    Path = input("Enter The Path : ")
                    os.system("attrib -h " + Path)
                    speak_only("Sir, All The Files in this folder are now visible to everyone.")
 
                elif 'leave it'in con or 'leave for now':
                    speak_only('OK')

# Location And Wether

            elif 'location' in query:
                from Back.Features import Location
                Location()

            elif 'weather' in query:
                from Back.Features import weather2
                weather2()

# YT

            elif 'youtube download' in query:
                def Finish():
                    print('Done Download!')
                from pytube import YouTube,Playlist
                import Back.speak as s
                import os
                s.speak("Press 1 For Video Download | Press 2 For Playlist Download | Press 3 For Audio Download | Press 4 For Quit")

                while True:
                    E = input("Enter Here : ")

                    if '1' in E:
                        s.speak("You Have Selected Video Download")
                        s.speak ("Please Enter URL")
                        URL1 = input("Enter URL Here : ")
                        s.speak ("Now Please Enter Path")
                        Path1 = input("Enter Path Here : ")
                        s.speak ("Now Please Enter resolution")
                        R1 = input("Enter Resolution Here : ")
                        Video = YouTube(URL1)
                        s.speak(f'Your Video Title Is : {Video.title}')
                        s.speak("Downloading........Please Wait For While")
                        video = Video.streams.get_by_resolution(R1)
                        video.download(Path1)  
                        s.speak(f"{Video.title} Has Being Downloaded IN {Path1}")
                        s.speak("DO YOU WHANT TO OPEN VIDEO DOWNLOADED Folder IF YES WRITE OPEN OR NO FOR NOT TO DOwNLOADED FOLDER OK ")
                        o = input("Enter Here : ")

                        if 'Yes' or 'y' or 'yes' or 'Y' in o:
                            os.startfile(Path1)

                        else:
                            exit()

                    elif '2' in E:
                        s.speak ("You Have Selected Playlist Download")
                        s.speak ("Please Enter URL")
                        URL2 = input("Enter URL Here : ")
                        s.speak ("Now Please Enter Path")
                        Path2 = input("Enter Path Here : ")
                        s.speak ("Now Please Enter resolution")
                        R2 = input("Enter Resolution Here : ")
                        Play = Playlist(URL2)
                        s.speak("Now Please Wait For While...............")
                        for video in Play.videos:
                            video.streams.get_by_resolution(R2).download(Path2)
                            video.register_on_complete_callback(Finish())
                        s.speak("All Download Completed")

                    elif '3' in E :
                        s.speak ("You Have Selected Audio Download")
                        s.speak ("Please Enter URL")
                        # url input from user
                        yt = YouTube(str(input("Enter URL Here : ")))

                        # extract only audio
                        video = yt.streams.filter(only_audio=True).first()

                        # check for destination to save file    
                        s.speak ("Now Please Enter Path")
                        destination = str(input("Enter Path Here : ")) or '.'

                        # download the file
                        out_file = video.download(output_path=destination)

                        # save the file
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)

                        # result of success
                        print( '                     ')
                        s.speak(yt.title + " has been successfully downloaded.")
                        
                    elif '4' in E:
                        break

# Phone Call 

            elif 'make a call' in query:
                from Phone.Call1 import call
                from Back.commands import takeCommand
                from Back.speak import speak
                speak('To whom?\n')
                person = input("Enter The Name : ") 
                call(person)

# mutiplication table

            elif 'table' in query:
                from Back.speak import speak_only
                speak_only("Please Enter Number : ")
                num =int(input("Please Enter Number : "))
                for i in range(2,(num+1)):
                    print("\n")
                    for j in range (1,11):
                        print(i,'x',j,'=',i*j),speak_only(f"{i},into,{j},=,{i*j}")

# Quit

            elif "goodbye jarvis" in query:
                ex_exit = "I feeling very sweet after meeting with you but you are going! i am very sad"
                speak_only(ex_exit)
                exit(ex_exit)

# Mini Games 

            elif "mini games" in query:
 
                from colored import fg, attr
                from colorama import Fore, Style
                from Back.commands import takeCommand
                from time import sleep

                bold = attr(1)
                reset = attr(0)
                gold = fg(226)
                orange = fg(202)
                green = fg(46)
                orange_4b = fg(94)
                
                speak("Sir Plase Wait For While I am Checking Any Mini Game Is There Or Not")
                sleep(2)
                speak("OK Sir i Got A Game The Game Name Is Guess The Number Do You Whant To Play This Game If Yes Say Yes If No Say No")
                q = takeCommand().lower()
                if "yes" in q:
                    import random
                    speak_only("Type a Number So That I can TakeA Number and The You Guess It Ok")
                    top_of_range = input(Fore.GREEN +f"{bold}\nType a number: "+ Style.RESET_ALL)

                    if top_of_range.isdigit():
                        top_of_range = int(top_of_range)

                        if top_of_range <= 0:
                            speak('Please type a number larger than 0 next time.')
                            quit()
                    else:
                        speak('Please type a number next time.')
                        quit()

                    random_number = random.randint(0, top_of_range)
                    guesses = 0

                    while True:
                        guesses += 1
                        user_guess = input(Fore.GREEN +f"{bold}\nMake a guess: "+ Style.RESET_ALL)
                        if user_guess.isdigit():
                            user_guess = int(user_guess)
                        else:
                            speak('Please type a number next time.')
                            continue

                        if user_guess == random_number:
                            speak("You got it!")
                            break
                        elif user_guess > random_number:
                            speak("You were above the number!")
                        else:
                            speak("You were below the number!")

                    speak(f"You got it in {guesses} guesses")
                else:
                    speak("OK")

# Password Mannegers

            elif "password" in query:
                from Back.speak import speak
                speak('Ok')
                from cryptography.fernet import Fernet


                def write_key():
                    key = Fernet.generate_key()
                    with open("key.key", "wb") as key_file:
                        key_file.write(key)

                def load_key():
                    file = open("key.key", "rb")
                    key = file.read()
                    file.close()
                    return key


                key = load_key()
                fer = Fernet(key)


                def view():
                    with open('passwords.txt', 'r') as f:
                        for line in f.readlines():
                            data = line.rstrip()
                            user, passw = data.split("|")
                            print("User:", user, " | Password:",
                                fer.decrypt(passw.encode()).decode())

                def add():
                    name = input('Account Name: ')
                    pwd = input("Password: ")

                    with open('passwords.txt', 'a') as f:
                        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

                while True:
                    mode = input(
                        "\nWould you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

                    if mode == "q":
                        break

                    if mode == "view":
                        view()

                    elif mode == "add":
                        add()

                    else:
                        print("Invalid mode.")
                        continue

# Jarvis reboot 

            elif 'restart' in query:
                speak("OK I Am Rebooting Myself")
                run()

run()