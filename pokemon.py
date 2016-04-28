from teknik import Teknik

class Pokemon:
    #============================================================================
    # Class data
    #============================================================================
    __states = set(["okay", "fainted", "asleep", "paralyzed", "confused",
                    "frozen", "burned", "poisoned"])

    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, name, number, poketype, tekniks,
                 base_hp, base_attack, base_defense, base_special, base_speed,
                 hp=None, attack=None, defense=None, special=None, speed=None,
                 state = "wait"):
        # set pokemon info
        self.name     = name
        self.number   = number
        self.poketype = poketype
        self.tekniks  = tekniks

        # set base stats
        self.base_hp      = base_hp
        self.base_attack  = base_attack
        self.base_defense = base_defense
        self.base_special = base_special
        self.base_speed   = base_speed

        # set current stats
        # these values can be zero, so check against None
        self.hp      = hp      if hp      is not None else base_hp
        self.attack  = attack  if attack  is not None else base_attack
        self.defense = defense if defense is not None else base_defense
        self.special = special if special is not None else base_special
        self.speed   = speed   if speed   is not None else base_speed

        # set the state
        self.__state = state

    def use_teknik(self, teknik, defender):
        """Uses a Teknik"""
        Teknik.use(teknik, self, defender)
        
    def take_damage(self, amount):
        """Take damage from a Teknik. Returns amount applied to pokemon."""

        # ASSERTIONS
        assert self.state != "fainted" # item/Teknik will have to revive first
        
        # dealt more than available, pokemon faints
        if amount >= self.hp:
            self.hp = 0
            self.state = "faint"
            amount -= self.hp
        else:
            self.hp -= amount

        return amount

    def heal_damage(self, amount):
        """Heals hp. Returns amount of hp healed."""

        # ASSERTIONS
        assert self.state != "fainted" # item/Teknik will have to revive first
        
        # can't heal more than the base_hp
        if self.hp + amount >= self.base_hp:
            amount = self.base_hp - self.hp
            self.hp = self.base_hp
        else:
            self.hp += amount

        return amount

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
            raise Exception("Invalid Pokemon state")
