class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number=1):
        if animal in self.animals:
            self.animals[animal] += number
        else:
            self.animals[animal] = number

    def get_info(self):
        for animal in self.animals.keys():
            print(f"{animal} : {self.animals[animal]}")

        return 'E I E I O'

    def get_animal_typs(self):
        animal_list = []
        for animal in self.animals.keys():
            animal_list.append(animal)
            animal_list.sort()
        return animal_list

    def get_short_info(self):
        animal_types = self.get_animal_typs()
        pluralized_animals = [
            animal + 's' if self.animals[animal] > 1 else animal for animal in animal_types
        ]
        animal_list = ', '.join(pluralized_animals)
        return f"{self.name}'s farm has {animal_list}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_typs())
print(macdonald.get_short_info())