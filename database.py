from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import config

class Database_Manager():
    def __init__(self):
        try:
            self.client = MongoClient(config.DATABASE_URL)
            self.db = self.client[config.DATABASE_NAME]
            self.collection = self.db[config.COLLECTION_NAME]
            print("mongodb O")
        except ConnectionFailure:
                print("mongodb X")
                raise
    def get_collection(self):
        return self.collection
    def close_collection(self):
        self.client.close()
        
db_manager = Database_Manager()
