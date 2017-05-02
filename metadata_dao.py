from util import Util

class Metadata_Dao:
    def __init__(self):
        self.util = Util()
        self.mongoConnection = self.util.getMongoClient()
        self.metadataColl = self.mongoConnection.metadata.metadata

    def fetchAllMetadata(self):
        metadata = self.metadataColl.find({})
        for m in metadata:
            print (m)