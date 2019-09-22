from pymongo import MongoClient
import pymongo
import pandas as pd
import numpy as np
import time

import src.tools.google as google
import src.tools.mongo as mongo
import src.constants as const
import src.tools.rating as rating
#Conexion to db

def main():

    db=const.getConstant("DB_CONEXION")

    # INITIAL FILTER

    getPossibleCities("companies",db)
    
    # FACILITIES get info from Google places
    google.getInfo(cities,properties,db,"facilities")

    # AIRPORTS

    #Import airports info and create geopoint colum
    airports=pd.read_csv("Input/airports.csv",header=None, usecols=[1,2,3,6,7,12])
    airports.columns=['Name','City','Country','latitude', 'longitude', 'Type']
    airports["geopoint"]=np.vectorize(mongo.geopoint)(airports["longitude"],airports["latitude"])
    
    #Load info in mongo
    coll=db["airports"] 
    coll.insert_many(airports.to_dict('record'))
    coll.create_index([('geopoint', pymongo.GEOSPHERE)])

    # PLACE RATING
    rating.rating(db)





if __name__=='__main__':
	main()