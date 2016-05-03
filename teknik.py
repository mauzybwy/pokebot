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
        self.__name     = name
        self.__tektype  = tektype
        self.__power    = power
        self.__category = category
        self.__accuracy = accuracy
        self.__base_pp  = base_pp
        self.__max_pp   = max_pp
        
    def use(self, attacker, defender):
        print attacker.name,
        print "used",
        print self.name        
        
        
        if tek.power and Pokecalc.evades(tek, attacker, defender):
            print "MISSED"
        else:
            self.__func(self, attacker, defender)
    
    #============================================================================
    # Properties
    #============================================================================
    @property
    def name():
        return self.__name

    @property
    def tektype():
        return self.__tektype
    
    @property
    def power():
        return self.__power

    @property
    def category():
        return self.__category

    @property
    def accuracy():
        return self.__accuracy

    @property
    def base_pp():
        return self.__base_pp

    @property
    def max_pp():
        return self.__max_pp
