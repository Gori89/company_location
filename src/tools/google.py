import time
import requests
import pandas as pd
import numpy as np

from src import constants as const
import src.tools.mongo as mongo
import src.tools.geo as geo

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

def mapping(result,googleType,name):
    info={}
    if 'name' in result:
        info["name"]=result['name']
    if 'geometry' in result:
        info["latitude"]=result['geometry']['location']['lat']
        info["longitude"]=result['geometry']['location']['lng']
    if 'rating' in result:
        info["rating"]=result['rating']
    info["googleType"]=googleType
    info["keyword"]=name
    return info

def getNearbyplaces(lat="",lon="",radius="",googleType="", name=""):
    res=nearby(lat,lon,radius,googleType,name)

    places=[]
    results=res['results']
    for i in range(len(results)):
        
        places.append(mapping(results[i], googleType,name))
    while ('next_page_token' in res):
        time.sleep(2)

        res=nearby(pagetoken=res["next_page_token"])
        results=res['results']

        for i in range(len(results)):
            places.append(mapping(results[i],googleType,name))

    return places

def getInfo(cities,properties,db,collectionName):
    for city in cities: #.city:
        for prop in properties.values():
            print(city)
            print(prop)
            coord=pd.DataFrame(db.offices.find({"city":city},{"latitude":1,"longitude":1,"_id":0}))
            grid_limit=[coord.latitude.max(),coord.latitude.min(),coord.longitude.max(),coord.longitude.min()]
            grid=geo.createGrid(grid_limit,prop["Radius"])
            df=(getPlaces(prop,grid))
            print(df.shape)
            print('Guardo el info ')
            df["geopoint"]=np.vectorize(mongo.geopoint)(df["longitude"],df["latitude"])
            mongo.loadDF(df,collectionName,db)

def getPlaces(placeType,grid):
    radius=placeType["Radius"]
    googleType=placeType['googleType']
    keyWords=placeType['Name']
    places=[]
    for lng in grid[1]:
        for lat in grid[0]:
            for elm in googleType:
                print(lat,lng,radius,elm,keyWords)
                places+=getNearbyplaces(lat,lng,radius,elm,keyWords)
                print(len(places))
    df=pd.DataFrame(places)
    return df[~df.duplicated()]
    