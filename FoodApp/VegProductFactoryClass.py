from ProductFactoryClass import ProductFactory
from VegBurgerClass import VegBurger
from VegPizzaClass import VegPizza
from VegNoodlesClass import VegNoodles

class VegProductFactory(ProductFactory):

    def createBurger(self, price: int, calories: int, descr: str):
        return VegBurger(price, calories, descr)

    def createPizza(self, price: int, calories: int, size: str, descr: str):
        return VegPizza(price, calories, size, descr)

    def createNoodles(self, price: int, calories: int, descr: str):
        return VegNoodles(price, calories, descr)
