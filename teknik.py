#from pokecalc import Pokecalc
#from teks import Teks

class Teknik:
    
    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, name, tektype, category, func,
                 power, accuracy, base_pp, max_pp):
        
        # give the Teknik some functionality
        self.__func = func

        # set info
        self.name     = name
        self.tektype  = tektype
        self.power    = power
        self.category = category
        self.accuracy = accuracy
        self.base_pp  = base_pp
        self.max_pp   = max_pp
        
    def use(self, attacker, defender):
        out = self.__func(self, attacker, defender)

        print attacker.name,
        print "used",
        print self.name,
        print ":",
        print out
        
        return out
        
    
    #============================================================================
    # Properties
    #============================================================================
