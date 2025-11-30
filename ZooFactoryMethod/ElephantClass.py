from IAnimalClass import IAnimal

class Elephant(IAnimal):
    def __init__(self):
        self.__name = "Elephant"

    def say(self):
        return f"{self.__name}: Trumpet"
