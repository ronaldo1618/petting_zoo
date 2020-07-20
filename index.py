from animals import Llama, Goat, Tiger, Monkey, Donkey, Turtle, Crocodile, Catfish, Seal, Carp, Python, Copperhead, RattleSnake, Cottonmouth, CoralSnake
from attractions import PettingZoo, SnakePit, Wetlands

# Naming attractions
varmint_village = PettingZoo('Varmint Village')
the_slither_inn = SnakePit('The Slither Inn')
critter_cove = Wetlands('Critter Cove')

# Naming animals and adding them to Petting Zoo
mizz_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "llama chow", 34)
billy = Goat("Billy", "american pygmy", "midday", "goat chow", 12)
tony = Tiger("Tony", "bengal tiger", "midday", "tiger chow", 32)
george = Monkey("George", "spider monkey", "night", "monkey chow", 23)
geoff = Donkey("Geoff", "donkey", "night", "donkey chow", 14)
varmint_village.add(mizz_fuzz)
varmint_village.add(billy)
varmint_village.add(tony)
varmint_village.add(george)
varmint_village.add(geoff)

# Naming animals and adding them to Wetlands
bruce = Turtle("Bruce", "turtle", "turtle chow", 65)
croc = Crocodile("Croc", "crocodile", "fish chow", 66)
willy = Catfish("Willy", "blue catfish", "fish chow", 67)
lucile = Seal("Lucile", "seal", "fish chow", 68)
big_mouth = Carp("Big Mouth", "asian carp", "fish chow", 69)
critter_cove.add(bruce)
critter_cove.add(croc)
critter_cove.add(willy)
critter_cove.add(lucile)
critter_cove.add(big_mouth)

# Naming animals and adding them to SnakePit
monty = Python("Monty", "snek", "snake chow", 76)
slitherin = Copperhead("Slitherin", "copperhead", "snake chow", 77)
venom = RattleSnake("Venom", "rattlesnake", "snake chow", 78)
mouf = Cottonmouth("Mouf", "cottonmouth", "snake chow", 79)
nemo = CoralSnake("Nemo", "coralsnake", "snake chow", 80)
the_slither_inn.add(monty)
the_slither_inn.add(slitherin)
the_slither_inn.add(venom)
the_slither_inn.add(mouf)
the_slither_inn.add(nemo)

# Print statements
print(f'{billy.name} the {billy.species} is available to pet during the {billy.shift} shift.')
print(bruce.feed())
print(mouf)
print(critter_cove)
print(the_slither_inn)
print(varmint_village)
print('The newest animal is', critter_cove.last_critter_added)