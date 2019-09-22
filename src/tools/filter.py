import pandas as pd
import src.constants as const
import src.tools.geo as geo
import src.tools.mongo as mongo
import numpy as np



def getPossibleCities():

    df_companies=mongo.getCompanies(mongo.localConection())

    # Delete unnecessary columns
    df_companies=df_companies.drop(columns=['permalink', 'crunchbase_url', 'homepage_url',
       'blog_url', 'blog_feed_url', 'twitter_username','tag_list',
       'alias_list', 'email_address', 'phone_number','created_at',
        'updated_at', 'overview', 'image', 'products',
       'relationships', 'competitions', 'providerships', 'total_money_raised',
        'milestones', 'video_embeds', 'screenshots',
       'external_links', 'partners'])

    # Delete closed companies 
    df_companies=df_companies[df_companies.deadpooled_year.isnull()]
    
    # Delete field no releted companies
    categories=const.getConstant("CATEGORIES")
    all_categories=categories[0]+categories[1]
    df_companies=df_companies[df_companies.category_code.isin(all_categories)]

    #get all the officies
    offices=[]
    for i in range(len(df_companies)):
        offices.append([df_companies.offices.iloc[i],df_companies._id.iloc[i]])
    office_list=[]

    for office in offices:
        a=pd.io.json.json_normalize(office[0])
        a["_id"]=office[1]
        office_list.append(a)
    df_office=pd.concat(office_list,sort=True)

    # Delete offices without lat. or long.
    df_office=df_office.dropna(subset=['latitude', 'longitude'])

    #Delete offices without city
    df_office["city_clean"]=df_office.city.apply(lambda x: str(x).replace(" City",""))
    df_office=df_office.drop("city",axis=1)
    df_office=df_office.rename(columns={"city_clean":"city"})

    filter_void=df_office.city=="" 
    filter_None=df_office.city=="None"
    df_office=df_office[~(filter_void | filter_None)]

    companies2=df_companies.merge(df_office, on="_id")
    companies2=companies2.drop(columns=["_id","offices"])

    cities=companies2[companies2.category_code.isin(categories[0])].city.value_counts()
    goodcities=cities[cities.values>=30]
    companies2=companies2[companies2.city.isin(goodcities.index)]

    companies2["geopoint"]=np.vectorize(mongo.geopoint)(companies2["longitude"],companies2["latitude"])

    companies2.to_json('Output/offices.json', orient="records")
    companies2.to_csv('Output/offices.csv', orient="records")
    mongo.loadDF(companies2,"offices",db)


