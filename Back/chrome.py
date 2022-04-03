import webbrowser as web
from Back.speak import speak_only
import os
from colorama import Fore, Style

def search_youtube(query):
    query = query.replace('youtube', "")
    query = query.lower()

    print(Fore.LIGHTYELLOW_EX + 'Opening YouTube and search about ' + Fore.LIGHTBLUE_EX + query + Style.RESET_ALL)
    speak_only(f'Opening YouTube and search about {query}')

    web.open('https://www.youtube.com/results?search_query=' + query)


def search_google(query):
    query = query.replace('google', '')
    query = query.lower()

    print(Fore.LIGHTYELLOW_EX + 'Opening Google and search about ' + Fore.LIGHTBLUE_EX + query + Style.RESET_ALL)
    speak_only(f'Opening google and search about {query}')

    web.open('https://www.google.com/search?q=' + query)