from datetime import date

#walking critters
class Llama:
    def __init__(self, name, species, shift, food, chip_num):
        self.__chip_num = chip_num
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True

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

class Goat:
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True
        self.__chip_num = chip_num

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

class Tiger:
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.__chip_num = chip_num
        self.walking = True

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

class Monkey:
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True
        self.__chip_num = chip_num

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

class Donkey:
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True
        self.__chip_num = chip_num

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

#swimming critters
class Turtle:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.__chip_num = chip_num
        self.food = food

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

class Crocodile:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.__chip_num = chip_num
        self.food = food

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

class Catfish:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.__chip_num = chip_num
        self.food = food

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

class Seal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.__chip_num = chip_num
        self.food = food

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

class Carp:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.__chip_num = chip_num
        self.food = food

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

#slithering critters
class Python:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.__chip_num = chip_num
        self.food = food

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

class Copperhead:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.__chip_num = chip_num
        self.food = food

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

class RattleSnake:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.__chip_num = chip_num
        self.food = food

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

class Cottonmouth:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.__chip_num = chip_num
        self.food = food

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

class CoralSnake:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.__chip_num = chip_num
        self.food = food

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