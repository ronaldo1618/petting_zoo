from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.__chip_num = chip_num
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()

    @property
    def chip_num(self):
        return self.__chip_num
    
    @chip_num.setter
    def chip_num(self, chip_num):
        pass

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"