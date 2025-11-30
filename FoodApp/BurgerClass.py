from IProductClass import IProduct

class Burger(IProduct):
    def __init__(self, price: int = 0, calories: int = 0, descr: str = ""):
        self._price = price
        self._calories = calories
        self._descr = descr

    def get_Price(self):
        return self._price

    def get_Description(self):
        return f"{self._descr} (Burger, {self._calories} cals, ${self._price})"
