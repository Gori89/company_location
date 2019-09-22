from geopy.geocoders import Nominatim
from math import sin, cos, sqrt, atan2, radians,ceil


def getCoord(place):
    geolocator = Nominatim(user_agent="SharkAttack")
    location = geolocator.geocode(place)
    return location[1]

def createGrid(grid_limit,radius):
    lat_dis=ceil(distance(grid_limit[0],grid_limit[2],grid_limit[1],grid_limit[2])/(radius/1000))
    lng_dis=ceil(distance(grid_limit[0],grid_limit[2],grid_limit[0],grid_limit[3])/(radius/1000))
    lat_space=(grid_limit[0]-grid_limit[1])/lat_dis
    lng_space=(grid_limit[2]-grid_limit[3])/lng_dis
    lng_row=[]
    lat_row=[]
    for lng in range(lng_dis+1):
        lng_row.append(grid_limit[2]-lng_space*lng)
    for lat in range(lat_dis+1):
        lat_row.append(grid_limit[0]-lat_space*lat)
    
    return [lat_row,lng_row]


def distance(lat1,lon1,lat2,lon2):

    R = 6373.0

    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
