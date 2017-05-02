import os

mongo_uri = os.environ["METADATA_URI"]

class Config:
    def __init__(self):
        self.config = {} #empty dictionary
        self.config['MONGO_URI'] = mongo_uri

    def getMongoUri(self):
        return self.config['MONGO_URI']