from IAnimalClass import IAnimal

class Lion(IAnimal):
    def __init__(self):
        self.__name = "Lion"

    def say(self):
        return f"{self.__name}: Roaring"
