from animals import Llama, Goat, Tiger, Monkey, Donkey, Turtle, Crocodile, Catfish, Seal, Carp, Python, Copperhead, RattleSnake, Cottonmouth, CoralSnake
from attractions import PettingZoo, SnakePit, Wetlands

# Naming attractions
varmint_village = PettingZoo('Varmint Village')
the_slither_inn = SnakePit('The Slither Inn')
critter_cove = Wetlands('Critter Cove')

# Naming animals and adding them to Petting Zoo
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

# Naming animals and adding them to Wetlands
bruce = Turtle("Bruce", "turtle", "turtle chow")
croc = Crocodile("Croc", "crocodile", "fish chow")
willy = Catfish("Willy", "blue catfish", "fish chow")
lucile = Seal("Lucile", "seal", "fish chow")
big_mouth = Carp("Big Mouth", "asian carp", "fish chow")
critter_cove.add(bruce)
critter_cove.add(croc)
critter_cove.add(willy)
critter_cove.add(lucile)
critter_cove.add(big_mouth)

# Naming animals and adding them to SnakePit
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

# Print statements
print(f'{billy.name} the {billy.species} is available to pet during the {billy.shift} shift.')
print(bruce.feed())
print(mouf)
print(critter_cove)
print(the_slither_inn)
print(varmint_village)