from .attraction import Attraction
from movements import Slithering

class SnakePit(Attraction):
        def __init__(self, name):
            self.description = 'sliterin sneks'
            Attraction.__init__(self, name)

        def add(self, animal):
            try:
                if animal.slither_speed > -1:
                    self.animals.append(animal)
            except AttributeError as ex:
                print(f'{animal} that doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')