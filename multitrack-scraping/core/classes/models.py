class Model:
    # checks for inheritance from class_to_check. (i.e. is self/the current instance a child of class_to_check?)
    def is_child_of(self, class_to_check: object):
        if (isinstance(self, type(class_to_check))):
            return True
        else:
            return False
    
    # does the reverse of is_child_of(). checks to see if class_to_check inherited from self/the current instance. (i.e. is self/the current instance the parent of class_to_check?)
    def is_parent_of(self, class_to_check: object):
        if (self.__class__.__instancecheck__(class_to_check)):
            return True
        else:
            return False
    
    @classmethod
    def get_class_dict(cls):
        return cls.__dict__
    
    def get_instance_dict(self):
        return self.__dict__