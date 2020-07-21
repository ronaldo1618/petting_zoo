from .animal import Animal
from movements import Swimming
from movements import Walking

class Crocodile(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def feed(self):
        return (f'Be sure to not HAND FEED the crocodiles like eight fingered JimBob. He\'s a professional. \n {self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')