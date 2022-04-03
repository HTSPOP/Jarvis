import webbrowser as web
from Back.speak import speak_only


def location(query):
    location = query.replace("my location","")
    speak_only('Locating' + location)
    web.open_new_tab("https://www.google.com/maps/p"+location)