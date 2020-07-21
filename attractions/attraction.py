class Attraction:

    def __init__(self, name):
        self.name = name
        self.animals = list()

    def remove(self, animal):
        self.animals.remove(animal)

    def __len__(self):
        return len(self.animals)

    def __str__(self):
            report = f'{self.name} is where you will find animals like:\n'
            for animal in self.animals:
                    report += f'  * {animal.name} the {animal.species}.\n'
            return report

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'