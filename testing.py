from pokemon import Pokemon
from pokecalc import Pokecalc
from teknik import Teknik
from battle import Battle
from trainer import Trainer

import threading

import yaml
import itertools

yml_file = "./res/pokes.yml"

with open(yml_file) as stream:
    pokes = yaml.load(stream)

pika1 = Pokemon(**pokes['Pikachu'])
pika2 = Pokemon(**pokes['Pikachu'])

trainer1 = Trainer("Bug Catcher", [pika1])
trainer2 = Trainer("Gary", [pika2])

def fake_battle(t1, t2):
    t1.fight(t2, "Tackle")
    while t2.state != "attack": pass
    t2.fight(t1, "Growl")
    while t1.state != "attack": pass
    t1.run()
    


b = Battle()

t = threading.Thread(target = b.begin, args=(trainer1, trainer2))
t.daemon=True
t.start()

t2 = threading.Thread(target = fake_battle, args=(trainer1, trainer2))
t2.daemon=True
t2.start()

t.join()
t2.join()
