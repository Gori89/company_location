import dotenv
import os
dotenv.load_dotenv()
key = os.getenv("GOOGLE_KEY")

constants={
    "NEAR_URL" : "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
    "GOOGLE_KEY" : key
}

def getConstant(name):
    try:
        return constants[name]
    except expression:
        return None
