from .queues import Queue


class Track:
    __tracks = {}
        
    @classmethod
    def update_track_id(cls, obj: object):
        cls.__tracks.update({obj: obj.track_id})
        return cls.__tracks
    
    @property
    def tracks(cls):
        return cls.__tracks
    
    def __init__(self):
        self.track_id = len(self.__tracks) + 1
        self.queue = Queue()
        
        self.update_track_id(self)