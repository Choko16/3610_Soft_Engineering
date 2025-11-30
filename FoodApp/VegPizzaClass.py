from PizzaClass import Pizza

class VegPizza(Pizza):
    def __init__(self, price: int, calories: int, size: str, descr: str) -> None:
        super().__init__(price, calories, size, descr)

    def showVegPizzaAdvert(self):
        return (
            f"Veg Pizza {self._size} size – {self._descr}, "
            f"{self._calories} cals for ${self._price}"
        )
