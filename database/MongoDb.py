import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDb():

    db_name = os.getenv("DB_NAME")
    db_uri = os.getenv("DB_URI_WEB")

    def __init__(self):
        self.client = pymongo.MongoClient(self.db_uri)
        self.mdb = self.client[self.db_name]
        print("Conectando...")
    
    def db(self):
        return self.mdb