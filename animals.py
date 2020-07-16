from datetime import date

#walking critters
class Llama:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Goat:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Tiger:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Monkey:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Donkey:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.food = food
        self.walking = True

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

#swimming critters
class Shark:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Crocodile:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dolphin:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Seal:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Carp:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

#slithering critters
class Python:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Copperhead:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class RattleSnake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Cottonmouth:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class CoralSnake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class PettingZoo:
        def __init__(self, name):
                self.name = name
                self.description = 'cute and fuzzy critters to cuddle'
                self.animals = list()

        def add(self, name):
                self.animals.append(name)

        def __str__(self):
                report = f'{self.name} is where you will find animals like:\n'
                for animal in self.animals:
                        report += f'  * {animal.name} the {animal.species}.\n'
                return report

class SnakePit:
        def __init__(self, name):
                self.name = name
                self.description = 'sliterin sneks'
                self.animals = list()

        def add(self, name):
                self.animals.append(name)

        def __str__(self):
                report = f'{self.name} is where you will find animals like:\n'
                for animal in self.animals:
                        report += f'  * {animal.name} the {animal.species}.\n'
                return report

class Wetlands:
        def __init__(self, name):
                self.name = name
                self.description = 'creatures of the wetlands'
                self.animals = list()

        def add(self, name):
                self.animals.append(name)

        def __str__(self):
                report = f'{self.name} is where you will find animals like:\n'
                for animal in self.animals:
                        report += f'  * {animal.name} the {animal.species}.\n'
                return report

varmint_village = PettingZoo('Varmint Village')
the_slither_inn = SnakePit('The Slither Inn')
critter_cove = Wetlands('Critter Cove')

mizz_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "llama chow")
billy = Goat("Billy", "american pygmy", "midday", "goat chow")
tony = Tiger("Tony", "bengal tiger", "midday", "tiger chow")
george = Monkey("George", "spider monkey", "night", "monkey chow")
geoff = Donkey("Geoff", "donkey", "night", "donkey chow")
varmint_village.add(mizz_fuzz)
varmint_village.add(billy)
varmint_village.add(tony)
varmint_village.add(george)
varmint_village.add(geoff)
bruce = Shark("Bruce", "great white", "fish chow")
croc = Crocodile("Croc", "crocodile", "fish chow")
willy = Dolphin("Willy", "dolphin", "fish chow")
lucile = Seal("Lucile", "seal", "fish chow")
big_mouth = Carp("Big Mouth", "asian carp", "fish chow")
critter_cove.add(bruce)
critter_cove.add(croc)
critter_cove.add(willy)
critter_cove.add(lucile)
critter_cove.add(big_mouth)
monty = Python("Monty", "snek", "snake chow")
slitherin = Copperhead("Slitherin", "copperhead", "snake chow")
venom = RattleSnake("Venom", "rattlesnake", "snake chow")
mouf = Cottonmouth("Mouf", "cottonmouth", "snake chow")
nemo = CoralSnake("Nemo", "coralsnake", "snake chow")
the_slither_inn.add(monty)
the_slither_inn.add(slitherin)
the_slither_inn.add(venom)
the_slither_inn.add(mouf)
the_slither_inn.add(nemo)
print(f'{billy.name} the {billy.species} is available to pet during the {billy.shift} shift.')
print(bruce.feed())
print(mouf)
print(critter_cove)
print(the_slither_inn)
print(varmint_village)