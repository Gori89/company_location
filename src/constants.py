import dotenv
import os
dotenv.load_dotenv()
key = os.getenv("GOOGLE_KEY")


'''paramiters to use in the search
    - Google place typs
    - keywords
    - radius of the search, also used to generet the grid of places to ask for
'''
properties={
    'Vegan':
    {'googleType': ["restaurant", "bar", "cafe", "meal_delivery", "meal_takeaway"],
    'Name': "Vegan" ,
    'Radius': 5000},
    
    'school':
    {'googleType': ["school"],
    'Name': "",
    'Radius': 5000},
        
    'starbucks':
    {'googleType': ["bar", "cafe", "meal_delivery", "meal_takeaway"],
    'Name': "starbucks",
    'Radius': 5000},
    
    'night_club':
    {'googleType': ['night_club'],
    'Name': "",
    'Radius': 5000}
}

'''Rating of locations 
    - Distance from the location
    - Name of the collection where the info is kepped
    - rating of the location according to the number of places in the area
    '''
rating={
    'Vegan':{
        'distance' : [1.5],
        'collection': 'facilities',
        'values':{
        5 : 10,
        4 : 8,
        3 : 6,
        2 : 4,
        1 : 2,
        0 : 0
        }
    },
    
    'school':{
        'distance' : [1.5],
        'collection': 'facilities',
        'values':{
        5 : 10,
        4 : 8,
        3 : 6,
        2 : 4,
        1 : 2,
        0 : 0
        }
    },
        
    'starbucks':{
        'distance' : [1.5],
        'collection': 'facilities',
        'values':{
        5 : 10,
        4 : 8,
        3 : 6,
        2 : 4,
        1 : 2,
        0 : 0
        }
    },
    
    'night_club':{
        'distance' : [1.5],
        'collection': 'facilities',
        'values':{
        5 : 10,
        4 : 8,
        3 : 6,
        2 : 4,
        1 : 2,
        0 : 0
        }
    },

    'airport':{
        'distance' : [20],
        'collection': 'airports',
        'values':{
        5 : 10,
        4 : 8,
        3 : 6,
        2 : 4,
        1 : 2,
        0 : 0
        }
    }

}

'''Ponderation of each aspect'''
ratio={
    'Vegan':10,
    'school':10,
    'starbucks':10,    
    'night_club':10,
    'airport':10
}

'''companies categoris related to our field'''
category=[["web","software","games_video"],["network_hosting","hardware","analytics","music",
          "cleantech","photo_video","design"]]

''' dict os constants'''
constants={
    "NEAR_URL" : "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
    "GOOGLE_KEY" : key,
    "PLACE_FILTER" : properties,
    "RATING" : rating,
    "GIRD_DENSITY" : 2000,
    "CATEGORIES" : category,
    "RATIO": ratio,
    "ANTI_DRAW": [40.4165000,-3.7025600]
}

''' Function that return the constants from the dictionary'''
def getConstant(name):
    try:
        return constants[name]
    except expression:
        return None

