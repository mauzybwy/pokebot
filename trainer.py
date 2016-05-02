from pokemon import Pokemon
from pokebelt import Pokebelt
from pokebelt import Pokebelt

class Trainer:
    #============================================================================
    # Class data
    #============================================================================
    __states = set(["atatck", "defend", "whiteout", "run"])
    
    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, name,  pokes, profile=None, state="defend"):
        self.name = name
        self.__profile = profile
        self.__state   = state

        self.__pokebelt = Pokebelt(pokes)

    def take_turn(self):
        self.state = "attack"

    def is_busy(self):
        return self.state == "attack"

    def is_leaving(self):
        return self.state == "run" or self.state == "whiteout"

    def fight(self, defender, teknik):
        self.__pokebelt.active_pokemon.fight(defender.active_pokemon(), teknik)
        self.state = "defend"

    def run(self):
        self.state = "run"

    def active_pokemon(self):
        return self.__pokebelt.active_pokemon

    def __change_pokemon():
        pass
    
    def __use_item(self, item):
        pass
    
    #============================================================================
    # Properties
    #============================================================================
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if value in __states:
            self.__state = value
        else:
            raise Exception("Invalid Trainer state")

