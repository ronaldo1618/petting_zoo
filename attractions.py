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