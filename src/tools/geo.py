from geopy.geocoders import Nominatim

def getCoord(place):
    geolocator = Nominatim(user_agent="SharkAttack")
    location = geolocator.geocode(place)
    return location[1]