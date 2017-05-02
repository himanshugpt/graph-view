
from config import config
from pymongo import MongoClient

class Util:

    def getMongoClient(self):
        con = config.Config()
        return MongoClient(con.getMongoUri())
