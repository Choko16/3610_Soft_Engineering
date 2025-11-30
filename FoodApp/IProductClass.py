from abc import ABC, abstractmethod


class IProduct(ABC):

    @abstractmethod
    def get_Price(self):
        pass

    @abstractmethod
    def get_Description(self):
        pass
