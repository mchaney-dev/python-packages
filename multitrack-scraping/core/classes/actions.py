import models
import time


class Action(models.Model):
    def __init__(self, **kwargs):
        self.CATEGORIES = []
        self.STATES = ['STOPPED', 'IDLE', 'RUNNING', 'DONE']
        self.__is_stopped = None
        self.__is_idle = None
        self.__is_running = None
        self.__is_done = None
        kwargs = {
            'category': None,
            'name': None
        }
        self.category = kwargs.get('category')
        self.__total_duration = None
        self.__time_remaining = None
        self.__time_elapsed = None
        self.__state = None
        self.name = kwargs.get('name')
        # TODO: add trigger list and object call, and parent queue and track getters

    @property
    def categories(self):
        return self.CATEGORIES
    
    @property
    def total_duration(self):
        return self.__total_duration
    
    @total_duration.setter
    def __set_total_duration__(self):
        def __calc_total_duration__():
            # TODO
            pass
    
    @property
    def time_elapsed(self):
        return self.__time_elapsed
    
    @time_elapsed.setter
    def __set_time_elapsed__(self):
        def __start_timer__():
            __start = time.time()
            return __start
        
        value = __start_timer__()
        self.__time_elapsed = value

    @property
    def time_remaining(self):
        return self.__time_remaining
    
    @time_remaining.setter
    def __set_time_remaining__(self):
        time_elapsed = self.__time_elapsed
        total_duration = self.__total_duration
        value = total_duration - time_elapsed
        self.__time_remaining = value
    
    @property
    def states(self):
        return self.STATES
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def __set_state__(self, value):
        def __is_valid__(value):
            for item in self.STATES:
                if (value == item):
                    return True
                else:
                    return False

        if (__is_valid__(value) is True):
            self.__state = value
            return 0
        else:
            return 1
        
        # TODO: while state is running, time it
        def __change_state__(self, queue_obj):
            pass
            # TODO: need to create queue class