import requests
from bs4 import BeautifulSoup
from Back.speak import speak_only,speak

def Temp():
    speak_only("Please Enter The Place Which Temperature Do You Whant To Get")
    place = input("Enter The Name Of Place : ")
    search = f'Weather In {place}'
    url = f'https://www.google.com/search?q={search}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    update = soup.find('div',class_ = "BNeawe").text
    speak(f"{search} Now Is {update}")
Temp()