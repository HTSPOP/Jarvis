import json
from urllib.request import urlopen
import Back.editables
from Back.speak import speak_only


def news():
    try:
        jsonObj = urlopen(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={Back.editables.newsAPIkey}")
        data = json.load(jsonObj)

        for item in data['articles']:
            speak_only(item['title'])

    except:
        speak_only('I can\'t search news at the moment')