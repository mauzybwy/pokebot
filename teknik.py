from pokecalc import Pokecalc

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
        print attacker.name,
        print "used",
        print self.name        
        
        
        if Pokecalc.evades(tek, attacker, defender):
            print "MISSED"
        else:
            self.__func(self, attacker, defender)
    
    #============================================================================
    # Properties
    #============================================================================
