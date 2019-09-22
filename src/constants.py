import dotenv
import os
dotenv.load_dotenv()
key = os.getenv("GOOGLE_KEY")

properties={
    'vegans':
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
    
    'Party':
    {'googleType': ['night_club'],
    'Name': "",
    'Radius': 5000}
}


rating={
    'vegans':{
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
    
    'Party':{
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

ratio={
    'vegans':10,
    'school':10,
    'starbucks':10,    
    'Party':10,
    'airport':10
}

category=[["web","software","games_video"],["network_hosting","hardware","analytics","music",
          "cleantech","photo_video","design"]]

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


def getConstant(name):
    try:
        return constants[name]
    except expression:
        return None

