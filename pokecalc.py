import random

class Pokecalc:
    randy = random.seed()

    @staticmethod
    def is_percent_chance(pct):
        return random.random() < pct
    
    @staticmethod
    def attack_random():
        """Random number between 0.85 and 1"""
        return random.random() * 0.15 + 0.85

    @staticmethod
    def type_eff(tek, defender):
        """
        Type Effectiveness.
        This can be either 0, 0.25, 0.5, 1, 2, or 4 depending on the type of attack
        and the type of the defending Pokemon.
        """
        return 1

    @staticmethod
    def STAB(tek, attacker):
        """
        Same-Type Attack Bonus. 
        This is equal to 1.5 if the attack is of the same type as the user, and 1 if otherwise.
        """
        return 1.5 if tek.tektype == attacker.poketype else 1

    @staticmethod
    def critical():
        """Critical Hit"""
        return 1

    @staticmethod
    def other(tek, attacker, defender):
        """
        Other counts for things like held items, Abilities, field advantages, and whether
        the battle is a Double Battle or Triple Battle or not.
        """
        return 1

    @staticmethod
    def modifier(tek, attacker, defender):
        """Attack damage modifier"""
        float_mod = ( Pokecalc.STAB(tek, attacker)
                      * Pokecalc.type_eff(tek, defender)
                      * Pokecalc.critical()
                      * Pokecalc.other(tek, attacker, defender)
                      * Pokecalc.attack_random())
        
        return float_mod

    @staticmethod
    def physical_ratio(attacker, defender):
        return attacker.attack / defender.defense

    @staticmethod
    def special_ratio(attacker, defender):
        return attacker.special / defender.defense

    @staticmethod
    def adjusted_level(attacker):
        """Adjusts level for calculating damage"""
        return (2 * attacker.level + 10) / 250.0        

    @staticmethod
    def damage(tek, attacker, defender, special = False):
        if special:
            ratio = Pokecalc.special_ratio(attacker, defender)
        else:
            ratio = Pokecalc.physical_ratio(attacker, defender)
        
        first_part =( Pokecalc.adjusted_level(attacker)
                      * ratio
                      * tek.power
                      + 2
        )

        mod = Pokecalc.modifier(tek, attacker, defender)
        
        return int(first_part * mod)

    @staticmethod
    def evades(tek, attacker, defender):
        return False
