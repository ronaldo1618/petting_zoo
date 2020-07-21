from .animal import Animal
from movements import Slithering
from datetime import date

class Python(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        return (f'Be careful feeding them... well... because snek. \n{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')