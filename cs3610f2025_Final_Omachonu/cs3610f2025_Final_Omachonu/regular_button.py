from button import Button
from observer import IObserver
from subject import ISubject

class RegularButton(Button, IObserver):
    def __init__(self, name: str) -> None:
        super().__init__("INACTIVE")
        self.__name = name
        self.__subscribed = False

    def click(self, subject: ISubject) -> None:
        
        if not self.__subscribed:
            subject.attach(self)
            self.__subscribed = True
            self.set_label("ACTIVE")
            print(f"{self.__name}: {self.label}")
        else:
            subject.detach(self)
            self.__subscribed = False
            self.set_label("INACTIVE")
            print(f"{self.__name}: {self.label}")

    def update(self, direction: str) -> None:
        self.move(direction)

    def move(self, direction: str) -> None:
        print(f"{self.__name} moves {direction}")
