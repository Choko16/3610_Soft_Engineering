from BurgerClass import Burger

class NonVegBurger(Burger):
    def __init__(self, price: int, calories: int, descr: str):
        super().__init__(price, calories, descr)
