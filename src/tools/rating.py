import src.constants as const
import src.tools.mongo as mongo
import src.tools.geo as geo
import pandas as pd
import numpy as np



def rate(lat,lng,db):
    '''Given a location and a type of place, the functión return a value(0-10) and the places used to make the rate'''
    aux = const.getConstant("RATING")
    raiting_places=pd.DataFrame()
    for place in aux.keys(): 
        raiting_places=raiting_places.append(mongo.getNearPlaces(place,lat,lng, aux[place]['distance'],aux[place]['collection'],db))
    
    raiting_places=raiting_places.drop(['_id'],axis=1)
    mongo.loadDF(raiting_places,"rating_facilities",db)
    return getRating(raiting_places,aux)

def getRating(places, rating):
    rating_values={}
    for place_type in rating.keys():
        rating_values[place_type]=getRating_per_place(places, place_type, rating[place_type])
    return rating_values
        
def getRating_per_place(places, place_type, rating):
    filter_googleType=places.googleType==place_type
    filter_keyword=places.keyword==place_type

    num=((filter_googleType | filter_keyword)).sum()
    if num > max(rating["values"].keys()):
        num=max(rating["values"].keys())
    return rating["values"][num]

def rateGrid(grid,db,city):
    result=[]
    for lng in grid[1]:
        for lat in grid[0]:
            a=rate(lat,lng,db)
            a['latitude']=lat
            a['longitude']=lng
            a['city']=city
            result.append(a)
    return result

def totalRate(row):
    ratio=const.getConstant("RATIO")
    a=[row[place]*ratio[place]for place in ratio.keys()]
    return(sum(a)/sum(ratio.values()))

def rating(db):
    coord_rating=[]
    cities=pd.DataFrame(db.offices.find({},{"city":1,"_id":0}))
    cities=cities[~cities.duplicated()]
    for city in cities.city:
        coord=pd.DataFrame(db.offices.find({"city":city},{"latitude":1,"longitude":1,"_id":0}))
        grid_limit=[coord.latitude.max(),coord.latitude.min(),coord.longitude.max(),coord.longitude.min()]
        grid=geo.createGrid(grid_limit,const.getConstant('GIRD_DENSITY'))
        rate=rateGrid(grid,db,city)
        coord_rating+=rate
    df=pd.DataFrame(coord_rating)
    df['total_Rating']=df.apply(totalRate,axis=1)
    df.to_csv('Output/rating.csv')
    df=df[df.total_Rating==max(df.total_Rating)]
    antiDraw=const.getConstant('ANTI_DRAW')
    df['Distance']=np.vectorize(geo.distance,excluded=('lat2','lon2'))(df.latitude,df.longitude,lat2=antiDraw[0],lon2=antiDraw[1])
    theplace=df[df.Distance==df.Distance.min()]  
    #Place Selection
    print("El mejor lugar para colocar la empresa es en "+theplace.city.iloc[0]+".")
    print("En las coordenadas: Latitud: {}, Longitud: {}".format(theplace.latitude.iloc[0],theplace.longitude.iloc[0]))

    return theplace




