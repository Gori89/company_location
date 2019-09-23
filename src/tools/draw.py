import src.constants as const
import pandas as pd
import folium


def cityHeatMap(city,specialPlace):
    rating=pd.read_csv('Output/rating.csv')
    rating=rating[['latitude','longitude','city','total_Rating']]
    city_center=rating.groupby('city').mean()
    map_city = folium.Map(location=[city_center.loc[city].latitude, city_center.loc[city].longitude],
     width=750, height=500, zoom_start=12)
    points=rating[rating.city==city]
    for i in range(len(points)):
        folium.Marker([points.iloc[i].latitude, points.iloc[i].longitude],
                        radius=2,
                        icon=folium.Icon(icon='1',color=rateColor(points.iloc[i].total_Rating)), 
                       ).add_to(map_city)
    
    folium.Marker([specialPlace.latitude, specialPlace.longitude],
                        radius=2,
                        icon=folium.Icon(icon='ok',color=rateColor(10)), 
                       ).add_to(map_city) 

    map_city.save('Output/map_'+city+'.html')
    return map_city

def rateColor(num):
    if num==10:
        return 'darkred'
    elif num>9:
        return 'red'
    elif num>8:
        return 'lightred'
    elif num>7:
        return 'orange'
    elif num>6:
        return 'darkgreen'
    elif num>5:
        return 'green'
    elif num>4:
        return 'lightgreen'
    elif num>3:
        return 'darkblue'
    elif num>2:
        return 'blue'
    elif num>1:
        return 'lightblue'
    else: return 'white'