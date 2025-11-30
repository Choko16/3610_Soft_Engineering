from FoodAppClass import FoodApp

def run_demo():
    app = FoodApp()

    order = [
        "VegBurger",
        "VegPizza",
        "VegNoodles",
        "NonVegBurger",
        "NonVegPizza",
        "NonVegNoodles",
        "NonVegCutlet"
    ]

    products = app.makeOrder(order)
    print(app.getOrderDescription(products))


if __name__ == "__main__":
    run_demo()
