from BurgerClass import Burger

class VegBurger(Burger):
    def __init__(self, price: int, calories: int, descr: str):
        super().__init__(price, calories, descr)

    def showVegBurgerAdvert(self):
        return f"Try our Veg Burger! {self._descr} ({self._calories} cals) only ${self._price}"
