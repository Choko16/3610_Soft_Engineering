from PizzaClass import Pizza

class NonVegPizza(Pizza):
    def __init__(self, price: int, calories: int, size: str, descr: str) -> None:
        super().__init__(price, calories, size, descr)
