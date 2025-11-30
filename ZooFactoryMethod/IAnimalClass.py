from abc import ABC, abstractmethod


class IAnimal(ABC):

    @abstractmethod
    def say(self):
        pass
