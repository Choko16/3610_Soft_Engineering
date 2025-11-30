from IAnimalClass import IAnimal

class Moose(IAnimal):
    def __init__(self):
        self.__name = "Moose"

    def say(self):
        return f"{self.__name}: Moooo"
