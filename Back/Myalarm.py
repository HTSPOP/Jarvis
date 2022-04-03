# from http.client import ImproperConnectionState
from Back.speak import speak_only
import datetime
import playsound
def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = altime[11:-3]
    horeal = altime[:2]
    horeal = int(horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    speak_only(f'Done , Alarm Is Set For {Timing}')
    while True:
        if horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                import webbrowser
                webbrowser.open("https://www.youtube.com/")
                import Back.application
                Back.application.close_chrome()
                Back.application.open_M()
                Back.application.close_M()
                Back.application.open_Blue()
                Back.application.close_Blue()
                import pyautogui
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                import random
                import os
                s3 = ['G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M1.wav','G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M2.wav']
                s4 = ['G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M3.wav','G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M4.wav']
                s5 = ['G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M1.wav','G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M6.wav']
                s6 = ['G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M7.wav','G:\\G:\Jarvis 4 (Without GUI)\\Alarm Music\\M8.wav']
                s7 = random.choice(s3)
                s8 = random.choice(s4)
                s9 = random.choice(s5)
                s10 = random.choice(s6)
                print(" ")
                print("I Am Playing :",s7)
                print(" ")
                print("I Am Playing :",s8)
                print(" ")
                print("I Am Playing :",s9)
                print(" ")
                print("I Am Playing :",s10)
                print(" ")
                playsound.playsound(s7)
                playsound.playsound(s8)
                playsound.playsound(s9)
                playsound.playsound(s10)
            elif Mireal<datetime.datetime.now().minute:
                import pyautogui
                speak_only("Alarm Is CLosed")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                speak_only("Wake Up Sir Or I Will Call Your Mom Or Dad ")
                import pyautogui
                pyautogui.press("volumedown")
                
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                break   

# if __name__ == '__main__':
#     alarm('06:00 PM')
