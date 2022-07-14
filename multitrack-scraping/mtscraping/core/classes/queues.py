from .actions import Action
from .helpers import Helper
from time import time


class Queue:
    __queues = {}
    
    @classmethod
    def update_queue_id(cls, obj: object):
        cls.__queues.update({obj: obj.queue_id})
        return cls.__queues
    
    @property
    def queues(cls):
        return cls.__queues
    
    def __init__(self):
        self.queue_id = len(self.__queues) + 1
        self.queue_list = {}
        self.current_item = None
        self.next_item = None
        self.action = Action()
        self.counter = None
        
        self.update_queue_id(self)
                
    def add_item(self):
        value = input('Enter url of webpage: \n')
        helper = Helper(value)

        def add_to_list():
            self.queue_list.update({helper.page_url: helper.response})
            list_keys = list(self.queue_list.keys())
                
            if (len(self.queue_list) > 0):
                self.current_item = list_keys[0]
                if (len(self.queue_list) > 1):
                    self.next_item = list_keys[1]
                            
        add_to_list()