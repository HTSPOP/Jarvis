import speech_recognition as sr
import speak
import os 
def hot():
    global listen
    listen = False
    r = sr.Recognizer()
    while True:
        while listen is False:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)  # Eliminating the noise.
                r.pause_threshold = 1
                audio = r.listen(source, timeout=20, phrase_time_limit=10)
            try:
                query = r.recognize_google(audio).lower()  # Converting speech to text
                if query == "jarvis":
                    listen = True
                    print("OK")
                    os.startfile('G:\Jarvis 3 (Without GUI)\Start.bat')
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
hot()