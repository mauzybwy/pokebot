from pokemon import Pokemon
from pokebelt import Pokebelt

class Trainer:
    #============================================================================
    # Class data
    #============================================================================
    __states = set(["atatck", "defend", "whiteout", "run"])
    
    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, profile, pokebelt=None, state="defend"):
        self.__profile = profile
        self.__state   = TrainerState(state)

        self.__pokebelt = pokebelt if pokebelt is not None else Pokebelt.basic_belt()

    def take_turn(self):
        self.state = "attack"

    def __fight(attacker, defender):
        pass

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

