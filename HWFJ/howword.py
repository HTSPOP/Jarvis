import struct
from time import sleep
import pyaudio
import pvporcupine
import pyttsx3
from colorama import Fore, Style
import editables
porcupine=None
paud=None
audio_stream=None

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[editables.gender].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', editables.rate)


def speak(audio):
    print(Fore.GREEN + str(audio) + Style.RESET_ALL)
    engine.say(audio)
    engine.runAndWait()


def speak_only(audio):
    engine.say(audio)
    engine.runAndWait()



try:
    access_key="5F2x/PYf/TrtmtS4G+wLxEpe8qqbmS7wkEeM3iICw6VbpLdN5fy1cA==" #to create access key signup to https://console.picovoice.ai/ 
    #new version of pvporcupine has a limitation--> you can use only in upto 3 devices in free version. 
    #you can install older version of pvporcupine --> pip install pvporcupine==1.9.5 , which does not require any access key
    #if you are using older version of pvporcupine, replace the below line with--> porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
    porcupine=pvporcupine.create(access_key=access_key,keywords=["jarvis"]) #pvporcupine.KEYWORDS for all keywords
    paud=pyaudio.PyAudio()
    audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    while True:
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index=porcupine.process(keyword)
        if keyword_index>=0:
            speak("OK I AM ONLINE")
            import os 
            os.startfile('P:\\jarvis-main\\Start.bat')
            sleep(3)
            speak("Now HotWord Is Offline Bye Sir")
            exit()
            

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()