from typing import List
from IProductClass import IProduct
from VegProductFactoryClass import VegProductFactory
from NonVegProductFactoryClass import NonVegProductFactory

class FoodApp:

    def __init__(self):
        self._availableFactories = {
            "veg": VegProductFactory(),
            "nonveg": NonVegProductFactory(),
        }

    def makeOrder(self, prodNames: List[str]):
        products: List[IProduct] = []

        for name in prodNames:
            key = name.lower().replace(" ", "")
            factory = None

            if key.startswith("veg"):
                factory = self._availableFactories["veg"]
            elif key.startswith("nonveg"):
                factory = self._availableFactories["nonveg"]

            if factory is None:
                print(f"Unknown product category: {name}")
                continue

            if "burger" in key:
                item = factory.createBurger(10, 400, f"{name} with fresh ingredients")
            elif "pizza" in key:
                item = factory.createPizza(12, 650, "Medium", f"{name} loaded with toppings")
            elif "noodles" in key:
                item = factory.createNoodles(9, 500, f"Hot {name}")
            elif "cutlet" in key:
                item = factory.createCutlet(6, 300, f"Crispy {name}")
            else:
                print(f"Food item {name} not recognized.")
                continue

            products.append(item)

        return products

    def getOrderDescription(self, products: List[IProduct]):
        lines = []
        total = 0

        for product in products:
            lines.append(product.get_Description())
            total += product.get_Price()

        lines.append(f"Total price: ${total}")
        return "\n".join(lines)
