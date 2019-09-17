import time
import requests
from src import constants as const

def validNum(num):
    try:
        float(num)
        return True
    except:
        return False


def nearby(lat="",lon="",radius="",googleType="", name="",pagetoken=""):
    '''
    makes a call to nearbysearch of google api and return 20 places
    '''
    nearByURL=const.getConstant("NEAR_URL")
    params={}
    if pagetoken!="":
        params['pagetoken']=pagetoken
    elif validNum(lat) and validNum(lon) and validNum(radius):
        #Mandatory if not pagetoken
        params['location']='{},{}'.format(lat,lon)
        params['radius']=str(radius)
        
        #Recomended
        if googleType!="":
            params['type']=googleType
        #Optional
        if name!='name':
            params['name']=name
        
    params['key']=const.getConstant("GOOGLE_KEY")

    if len(params)==0:
        raise ValueError  
    res=requests.get(nearByURL, params=params).json()
    
    return res

def mapping(result):
    info={}
    if 'name' in result:
        info["name"]=result['name']
    if 'geometry' in result:
        info["geometry"]=result['geometry']['location']
    if 'rating' in result:
        info["rating"]=result['rating']
    return info

def getNearbyplaces(lat="",lon="",radius="",googleType="", name=""):
    res=nearby(lat,lon,radius,googleType,name)

    places=[]
    results=res['results']
    for i in range(len(results)):
        places.append(mapping(results[i]))
    while ('next_page_token' in res):
        time.sleep(2)

        res=nearby(pagetoken=res["next_page_token"])
        results=res['results']

        for i in range(len(results)):
            places.append(mapping(results[i]))

    return places
    