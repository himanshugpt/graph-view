import logging

from util import util
from modals import metadata

log = logging.getLogger(__name__)

class Metadata_Dao:
    def __init__(self):
        self.util = util.Util()
        self.mongoConnection = self.util.getMongoClient()
        self.metadataColl = self.mongoConnection.metadata.metadata

    def fetchAllMetadata(self):
        metadata_result = self.metadataColl.find({})
        metadata_list = []
        for m in metadata_result:
            metadata_list.append(metadata.Metadata.get_object(m))
        return  metadata_list