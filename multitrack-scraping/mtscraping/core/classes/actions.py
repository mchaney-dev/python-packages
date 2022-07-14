class Action:
    __actions = {}
    __allowed_types = ['get', 'filter', 'search', 'download', 'upload']
    
    @classmethod
    def update_action_id(cls, obj: object):
        cls.__actions.update({obj: obj.action_id})
        return cls.__actions
    
    @property
    def actions(cls):
        return cls.__actions
                
    @property
    def allowed_types(cls):
        return cls.__action_types
    
    def __init__(self):
        self.action_id = len(self.__actions) + 1
        self.action_list = {}
        self.action_type = self.get_type()
        self.state = self.State()
        
        self.update_action_id(self)
                    
    def get_type(self):
        action_types = ['get', 'filter', 'search', 'download', 'upload']
        pass
                
    class State:
        __states = ['RUNNING', 'DONE', 'IDLE', 'ERROR']
    
        @property
        def states(cls):
            return cls.__states
    
        def __init__(self):
            self.current_state = 'IDLE'
            self.progress = None
            self.counter = None
                        
        def __state_checker__(self, state_to_check: str):
            def __has_valid_state__():
                if (self.current_state in self.__states):
                    return True
                else:
                    return False
                            
            if (__has_valid_state__):
                if (self.current_state == state_to_check):
                    return True
                else:
                    return False
                            
        @property
        def is_running(self):
            return self.__state_checker__('RUNNING')
                    
        @property
        def is_done(self):
            return self.__state_checker__('DONE')
                    
        @property
        def is_idle(self):
            return self.__state_checker__('IDLE')
                    
        @property
        def is_error(self):
            return self.__state_checker__('ERROR')