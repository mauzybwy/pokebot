import yaml
import pprint
import itertools

pp = pprint.PrettyPrinter(indent=4)

yml_file = "./res/pokes.yml"

with open(yml_file) as stream:
    for poke, value in yaml.load(stream).iteritems():
        p = Pokemon(**value)
        print p
    
