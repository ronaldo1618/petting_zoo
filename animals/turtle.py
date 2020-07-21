from .animal import Animal
from movements import Walking
from movements import Swimming

class Turtle(Animal, Walking, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)