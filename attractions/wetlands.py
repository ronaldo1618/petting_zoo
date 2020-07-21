from .attraction import Attraction
from movements import Swimming

class Wetlands(Attraction):
        def __init__(self, name):
            self.description = 'creatures of the wetlands'
            super().__init__(name)

        def add(self, animal):
            try:
                if animal.swim_speed > -1:
                    self.animals.append(animal)
            except AttributeError as ex:
                print(f'{animal} that doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')