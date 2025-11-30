from IAnimalClass import IAnimal

class GrizzlyBear(IAnimal):
    def __init__(self):
        self.__name = "Grizzly Bear"

    def say(self):
        return f"{self.__name}: GROWL"
