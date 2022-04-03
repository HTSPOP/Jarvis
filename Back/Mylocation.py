import requests
from Back.speak import speak_only,speak
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
def My_location():

    ip_add = requests.get('https://api.ipify.org').text

    URL = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'

    geo_q = requests.get(URL)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f'Sir , You Are in {state,country}.')

def GoogleMaps(Place):
    URL_Place = 'https://www.google.com/maps/place/'+str(Place) 
    geolocator = Nominatim(user_agent='myGeocoder')
    location = geolocator.geocode(Place,addressdetails=True)
    target= location.latitude,location.longitude
    location = location.raw['address']
    web.open(url=URL_Place)
    target2 = {'city': location.get('city',''),
                    'state': location.get('state',''),
                    'country': location.get('country','')}

    current = geocoder.ip('me')
    current_latlon = current.latlng
    distance = str(great_circle(current_latlon,target))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    speak(f'\nSir , {Place} is {distance} kilometre Away From Your Location')


