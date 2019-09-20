from pymongo import MongoClient
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
     