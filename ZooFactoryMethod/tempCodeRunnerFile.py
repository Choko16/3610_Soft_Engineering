from IZooClass import IZoo
from AnimalsFactoryClass import AnimalsFactory

class Toronto_Zoo(IZoo):
    def __init__(self):
        super().__init__()
        self._ourItinerary = (
            "Welcome to the Toronto Zoo! "
            "Our Itinerary: 1) African Savanna. 2) Tundra Trek"
        )

    def create_Animals(self):
        
        animal_types = ["lion", "elephant", "penguin", "whitebear"]
        self._animals = []

        for t in animal_types:
            animal = AnimalsFactory.create_Animal(t)
            if animal:
                self._animals.append(animal)
