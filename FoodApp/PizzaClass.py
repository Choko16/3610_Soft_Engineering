from IProductClass import IProduct

# Abstract Product: Pizza
class Pizza(IProduct):
    def __init__(self, price: int = 0, calories: int = 0, size: str = "Small", descr: str = "") -> None:
        self._price = price
        self._calories = calories
        self._size = size
        self._descr = descr

    def get_Price(self):
        return self._price

    def get_Description(self):
        return (
            f"{self._descr} (Pizza, size: {self._size}, "
            f"{self._calories} cals, ${self._price})"
        )
