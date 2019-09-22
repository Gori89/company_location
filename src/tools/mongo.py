from pymongo import MongoClient
import pymongo
import pandas as pd
import src.tools.geo as geo


def localConection():
    '''
    Conectión to mongo's local server
    '''
    return MongoClient("mongodb://localhost:27017/")

def getCompanies(client):
    '''
    recover companies collection in a DataFrame
    '''
    companies = client.companies.companies.find()
    return pd.DataFrame(companies)

def geopoint(long, lat): 
    return {"type": "Point", "coordinates": [long,lat]}

def farPoints(city,radius):
    coord=geo.getCoord(city)
    radius
    return {"city":city,
     "geopoint":{"$not":{"$geoWithin":
    { "$centerSphere": [ [ coord[1], coord[0] ], (radius*0.621371)/3963.2 ]}
                        }}}

def loadDF(df,collectionName,db):
    coll=db[collectionName] 
    coll.insert_many(df.to_dict('record'))
    coll.create_index([('geopoint', pymongo.GEOSPHERE)])


def getPlacesCircle(place,lat,lng, radius, collection,db):
    
    return db[collection].find({'$or':[{'googleType':place},{'keyword':place}],
    'geopoint': {'$geoWithin':
                 { '$centerSphere': [ [ lng,lat ], (radius*0.621371)/3963.2 ]}}})

def getNearPlaces(place,lat,lng, distance, collection,db):
    df=pd.DataFrame()
    for radius in distance:
        aux=getPlacesCircle(place,lat,lng, radius, collection,db)
        df_aux=pd.DataFrame(aux)
        if not df_aux.empty:
            df_aux.insert(4,"distance", radius)
            df_aux.insert(5,"org_lat", lat)
            df_aux.insert(6,"org_lng", lng)
            df=df.append(df_aux)
    #quitar duplicados
    return df[~df.duplicated(subset=['googleType','latitude','longitude','name'],keep='first')]

     