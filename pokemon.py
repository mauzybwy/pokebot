import itertools
from teknik import Teknik
from teks import Teks

class Pokemon:
    #============================================================================
    # Class data
    #============================================================================
    __states = set(["okay", "fainted", "asleep", "paralyzed", "confused",
                    "frozen", "burned", "poisoned"])

    #============================================================================
    # Instance data
    #============================================================================
    def __init__(self, name, number, poketype, tekniks, level,
                 base_hp, base_attack, base_defense, base_special, base_speed,
                 state = "new",
                 stat_stages = {
                     'attack'   : 0,
                     'defense'  : 0,
                     'special'  : 0,
                     'speed'    : 0,
                     'accuracy' : 0,
                     'evasion'  : 0
                 }):

        # the only part of a Teknik that changes for a Pokemon is the pp field
        self.__tekniks = {}
        for key, value in tekniks.iteritems():
            self.__tekniks[key] = value if value >= 0 else Teks.teks[key].base_pp
        
        # set pokemon info
        self.__name     = name
        self.__number   = number
        self.__poketype = poketype
        self.__level    = level

        self.__stat_stages = stat_stages

        # set base stats
        self.__base_hp      = base_hp
        self.__base_attack  = base_attack
        self.__base_defense = base_defense
        self.__base_special = base_special
        self.__base_speed   = base_speed

        # set current stats
        self.__hp      = hp      if hp      is not None else base_hp
        
        # set the state
        self.__state = state

    def fight(self, defender, teknik):
        """Uses a Teknik"""

        Teks.teks[teknik].use(self, defender)

        
    def take_damage(self, amount):
        """Take damage from a Teknik. Returns amount applied to pokemon."""

        # ASSERTIONS
        assert self.state != "fainted" # item/Teknik will have to revive first
        
        # dealt more than available, pokemon faints
        if amount >= self.__hp:
            self.__hp = 0
            self.__state = "faint"
            amount -= self.__hp
        else:
            self.__hp -= amount

        return amount

    def heal_damage(self, amount):
        """Heals hp. Returns amount of hp healed."""

        # ASSERTIONS
        assert self.__state != "fainted" # item/Teknik will have to revive first
        
        # can't heal more than the base_hp
        if self.__hp + amount >= self.__base_hp:
            amount = self.__base_hp - self.__hp
            self.__hp = self.__base_hp
        else:
            self.__hp += amount

        return amount

    def __stage_multiplier(self, stat):
        stage = self.__stat_stages[stat]
        
        ratio = (2 + abs(stage))/2

        return ratio if stage >= 0 else (1 / ratio)
        
    
    def shift_stat(self, stat, amount):
        # don't do anything if there is no actual change
        if amount == 0:
            return
        
        curr = self.__stat_stages[stat]
        sign = -1 if curr < 0 else 1

        # do all math with positive numbers, apply sign at end
        if amount < 0:
            amount = abs(amount)
            
        if abs(curr) >= 6:
            print "Nothing happened!"
            self.__stat_stages[stat] = 6 * sign # correct, just in case
        else:
            total = curr + amount
            if total > 6:
                amount = 6 - curr

            # prepare to print the qualitative amount risen/fallen
            if amount == 1:
               qual_amt = " "
            elif amount == 2:
                qual_amt = " greatly "
            elif amount >= 3:
                qual_amt = " severely "
            else:
                raise Exception("Error in calculating stat change")

            # prepare to print whether the stat has risen or fallen
            direction = "rose!" if sign > 0 else "fell!"

            # actually apply the change
            self.__stat_stages[stat] += (amount * sign)
            
            # print message
            print self.name + "'s " + stat + qual_amt + direction
        
    #============================================================================
    # Properties
    #============================================================================
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        assert self.__state != "fainted"
        
        if value in __states:
            self.__state = value
        else:
            raise Exception("Invalid Pokemon state")

    @property
    def attack(self):
        return int(self.__attack * self.__stage_multiplier('attack'))

    @property
    def defense(self):
        return int(self.__defense * self.__stage_multiplier('defense'))
    
    @property
    def special(self):
        return int(self.__special * self.__stage_multiplier('special'))
    
    @property
    def speed(self):
        return int(self.__speed * self.__stage_multiplier('speed'))

    @property
    def evasion(self):
        return self.__stage_multiplier('accuracy')
    
    @property
    def accuracy(self):
        return self.stage_multiplier('evasion')
