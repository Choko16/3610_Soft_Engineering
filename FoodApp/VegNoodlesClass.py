from IProductClass import IProduct

class VegNoodles(IProduct):
    def __init__(self, price: int, calories: int, descr: str):
        self._price = price
        self._calories = calories
        self._descr = descr

    def get_Price(self):
        return self._price

    def get_Description(self):
        return f"{self._descr} (Veg Noodles, {self._calories} cals, ${self._price})"
