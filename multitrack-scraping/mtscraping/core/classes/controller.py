from .tracks import Track


class Controller:
    __instances = {}
    
    @classmethod
    def update_instance(cls, obj: object):
        cls.__instances.update({obj: obj.instance})
        return cls.__instances
    
    @property
    def instances(cls):
        return cls.__instances
    
    def __init__(self):
        self.instance = len(self.__instances) + 1
        self.track = Track()
        
        self.update_instance(self)
