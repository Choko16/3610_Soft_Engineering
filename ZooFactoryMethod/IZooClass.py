from abc import ABC, abstractmethod
from typing import List

from IAnimalClass import IAnimal


class IZoo(ABC):

    def __init__(self):
        self._animals: List[IAnimal] = []
        self._ourItinerary: str = ""

    @abstractmethod
    def create_Animals(self):
        pass

    def askEachAnimalSaySomething(self):
        for animal in self._animals:
            print(animal.say())

    def startVisit(self):
        self.create_Animals()
        print(self._ourItinerary)
        print("Animals you will see today:")
        self.askEachAnimalSaySomething()
