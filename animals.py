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

#walking critters
class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

class Tiger(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

class Monkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        return (f'Will still basket of food if not careful. Keep an eye on the food at all times! \n{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

#swimming critters
class Turtle(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Crocodile(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        return (f'Be sure to not HAND FEED the crocodiles like eight fingered JimBob. He\'s a professional. \n {self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Catfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Seal(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Carp(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

#slithering critters
class Python(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        return (f'Be careful feeding them... well... because snek. \n{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Copperhead(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class RattleSnake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Cottonmouth(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class CoralSnake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True