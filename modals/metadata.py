import logging

log = logging.getLogger(__name__)

class Metadata:
    def __init__(self):
        self._id = None
        self.last_successful_runtime = None
        self.exception = None
        self.last_successful_end_time = None
        self.last_ping_time = None
        self.last_start_time = None
        self.state = None
        self.depends_on = []

    @staticmethod
    def get_object(data):
        metadata = Metadata()
        for field in metadata.__dict__.keys():
            if data.get(field):
                setattr(metadata, field, data.get(field))
        return metadata