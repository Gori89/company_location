from pymongo import MongoClient
import pymongo
import pandas as pd
import numpy as np
import time

import src.tools.google as google
import src.tools.mongo as mongo
import src.constants as const
import src.tools.rating as rating
import src.tools.draw as draw
#Conexion to db

def main():

    db=const.getConstant("DB_CONEXION")

    # INITIAL FILTER
    # keep only active and related companies
    getPossibleCities("companies",db)
    
    # FACILITIES 
    # Get info from Google places to get near places
    # The paramiters of the search can be set in constants
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
    # For each city, a grid covering al the companies in that city is genereted
    # The points of the grid are rated
    # Settings of the rating can be change in constants
    theplace=rating.rating(db)

    # Generate Map
    # Heat map of each point in the grid of the city with the best place
    # The best palce is marked with a tick
    draw.cityHeatMap(theplace.city.iloc[0],theplace)





if __name__=='__main__':
	main()