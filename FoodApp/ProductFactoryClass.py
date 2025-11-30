from abc import ABC, abstractmethod
from BurgerClass import Burger
from PizzaClass import Pizza
from IProductClass import IProduct

class ProductFactory(ABC):

    @abstractmethod
    def createBurger(self, price: int, calories: int, descr: str):
        pass

    @abstractmethod
    def createPizza(self, price: int, calories: int, size: str, descr: str):
        pass

    def createNoodles(self, price: int, calories: int, descr: str):
        raise NotImplementedError("This factory does not support noodles.")

    def createCutlet(self, price: int, calories: int, descr: str):
        raise NotImplementedError("This factory does not support cutlet.")
