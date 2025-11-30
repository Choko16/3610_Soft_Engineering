from IZooClass import IZoo
from AnimalsFactoryClass import AnimalsFactory


class Calgary_Zoo(IZoo):
    def __init__(self):
        super().__init__()
        self._ourItinerary = (
            "Welcome to the Calgary Zoo! "
            "Our Itinerary: 1) Penguin Plunge. 2) Wild Canada"
        )

    def create_Animals(self):
        animal_types = ["grizzlybear", "moose", "penguin"]
        self._animals = []

        for t in animal_types:
            animal = AnimalsFactory.create_Animal(t)
            if animal:
                self._animals.append(animal)
