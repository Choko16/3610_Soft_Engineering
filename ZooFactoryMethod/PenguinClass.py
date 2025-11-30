from IAnimalClass import IAnimal

class Penguin(IAnimal):
    def __init__(self) -> None:
        self.__name = "Penguin"

    def say(self):
        return f"{self.__name}: qwaak"
