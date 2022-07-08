import actions


class trigger(actions.Action):
    def __init__(self, *args, **kwargs):
        args = []
        # TODO: fix args and kwargs
        
        self.CONDITION_TYPES = []
        self.CONDITION_ARGS = []
        self.action = Action()