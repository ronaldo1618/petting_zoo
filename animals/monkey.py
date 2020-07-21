from .animal import Animal
from movements import Walking

class Monkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        return (f'Will still basket of food if not careful. Keep an eye on the food at all times! \n{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')