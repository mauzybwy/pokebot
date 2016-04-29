import random

class Teknik:
    #============================================================================
    # Tekniks
    #============================================================================    
    randy = random.seed()    
    
    def __physical(tek, attacker, defender):
        print tek.name

    
    #============================================================================
    # Class data
    #============================================================================    
    tektable = {
        'tackle': __physical
    }

    
    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, name,
                 base_power, base_accuracy, base_pp,
                 power=None, accuracy=None, pp=None):

        # Tekniks get there functionality from the table, so the function must exist there
        if name not in __tektable:
            raise Exception("Teknik not found!")

        # give the Teknik some functionality
        self.__func = __tektable[name]

        # set info
        self.name  = name

        # set base stats
        self.base_power    = base_power
        self.base_accuracy = base_accuracy
        self.base_pp       = base_pp
        
        # set current stats
        self.power    = power    if power    is not None else base_power
        self.accuracy = accuracy if accuracy is not None else base_accuracy
        self.pp       = pp       if pp       is not None else base_pp

    def use(self, attacker, defender):
        return self.__func(self, attacker, defender)
    
    #============================================================================
    # Properties
    #============================================================================
