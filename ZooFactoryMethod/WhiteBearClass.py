from IAnimalClass import IAnimal

class WhiteBear(IAnimal):
    def __init__(self):
        self.__name = "White Bear"

    def say(self):
        return f"{self.__name}: Grrr"
