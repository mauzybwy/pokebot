from pokemon import Pokemon

class Pokebelt:
    #============================================================================
    # Class data
    #============================================================================
    def basic_belt():
        pass
    
    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, pokes):
        if not pokes:
            raise Exception("No pokemon!")
        if len(pokes) > 6:
            raise Exception("Too may pokemon!")
        
        self.__pokes = pokes
        self.__active_pokemon = pokes[0]

    def choose(self, poke):
        pass

    #============================================================================
    # Properties
    #============================================================================
    @property
    def active_pokemon(self):
        return self.__active_pokemon
