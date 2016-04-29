#from pokemon import Pokemon
#from pokecalc import Pokecalc
#from teknik import Teknik
import yaml
import itertools

yml_file = "./res/pokes.yml"

with open(yml_file) as stream:
    pokes = yaml.load(stream)

attacker = Pokemon(**pokes['Pikachu'])
defender = Pokemon(**pokes['Pikachu'])

attacker.fight(defender, 'Tackle')
attacker.fight(defender, 'Growl')
attacker.fight(defender, 'Thunder Shock')
