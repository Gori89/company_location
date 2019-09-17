from pymongo import MongoClient
import pandas as pd


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
     