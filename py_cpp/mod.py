
class Mod:
    """ Dummy class. """
    def __init__(self, dummy):
        self._dummy = dummy
    
    @property
    def dummy(self):
        return self._dummy

    @dummy.setter
    def dummy(self, dummy):
        self._dummy = dummy
    
    def return_five(self):
        return 5