import random
import playsound
import time
while True:
    s = ["P:\\jarvis-main\\Music\\01.wav","P:\\jarvis-main\\Music\\02.wav",
        "P:\\jarvis-main\\Music\\03.wav","P:\\jarvis-main\\Music\\04.wav",
        "P:\\jarvis-main\\Music\\05.wav","P:\\jarvis-main\\Music\\06.wav",
        "P:\\jarvis-main\\Music\\07.wav","P:\\jarvis-main\\Music\\08.wav",
        "P:\\jarvis-main\\Music\\09.wav","P:\\jarvis-main\\Music\\10.wav",
        "P:\\jarvis-main\\Music\\11.wav","P:\\jarvis-main\\Music\\12.wav",
        "P:\\jarvis-main\\Music\\13.wav","P:\\jarvis-main\\Music\\14.wav",
        "P:\\jarvis-main\\Music\\15.wav","P:\\jarvis-main\\Music\\16.wav",
        "P:\\jarvis-main\\Music\\17.wav","P:\\jarvis-main\\Music\\18.wav",
        "P:\\jarvis-main\\Music\\19.wav","P:\\jarvis-main\\Music\\20.wav",
        "P:\\jarvis-main\\Music\\21.wav","P:\\jarvis-main\\Music\\22.wav",
        "P:\\jarvis-main\\Music\\23.wav","P:\\jarvis-main\\Music\\24.wav",
        "P:\\jarvis-main\\Music\\25.wav","P:\\jarvis-main\\Music\\26.wav",
        "P:\\jarvis-main\\Music\\27.wav","P:\\jarvis-main\\Music\\28.wav",
        "P:\\jarvis-main\\Music\\29.wav","P:\\jarvis-main\\Music\\30.wav",
        "P:\\jarvis-main\\Music\\31.wav","P:\\jarvis-main\\Music\\32.wav"]
    s1 = random.choice(s)
    print("    ")
    print("I Am Playing :", s1)
    print("    ")
    playsound.playsound(s1)


#     # R = sr.Recognizer()
#     #     import speak

#     #     with sr.Microphone() as source:
#     #         print("                    ")
#     #         print(Fore.YELLOW + "Listening...." + Style.RESET_ALL)
#     #         audio = R.listen(source)
#     #     try:
#     #         print("                    ")
#     #         print(Fore.YELLOW + "Recognizing...." + Style.RESET_ALL)
#     #         text = R.recognize_google(audio, language="en-in")
#     #         print("                    ")
#     #         print(Fore.LIGHTMAGENTA_EX + "User Said : >> ", text + Style.RESET_ALL)
#     #     except Exception:
#     #         print("                    ")
#     #         print(Fore.YELLOW + "Please tell again" + Style.RESET_ALL)
#     #         return "None"
#     #     text = text.lower()
#     #     return text

# import speak
# import time
# import playsound
# speak.speak_only("Ok Please Wait For 2 second")
# time.sleep(2)                    
# playsound.playsound("P:\\jarvis-main\\Music\\32.wav")