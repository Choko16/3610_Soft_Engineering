from ProductFactoryClass import ProductFactory
from NonVegBurgerClass import NonVegBurger
from NonVegPizzaClass import NonVegPizza
from NonVegNoodlesClass import NonVegNoodles
from NonVegCutletClass import NonVegCutlet

class NonVegProductFactory(ProductFactory):

    def createBurger(self, price: int, calories: int, descr: str):
        return NonVegBurger(price, calories, descr)

    def createPizza(self, price: int, calories: int, size: str, descr: str):
        return NonVegPizza(price, calories, size, descr)

    def createNoodles(self, price: int, calories: int, descr: str):
        return NonVegNoodles(price, calories, descr)

    def createCutlet(self, price: int, calories: int, descr: str):
        return NonVegCutlet(price, calories, descr)
