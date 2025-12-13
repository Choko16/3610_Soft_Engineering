from button import Button
from control_button_publisher import ControlButtonPublisher

class ControlButton(Button):
    def __init__(self, label: str, direction: str, publisher: ControlButtonPublisher) -> None:
        super().__init__(label)
        self.__direction = direction
        self.__publisher = publisher

    def click(self) -> None:
        
        self.__publisher.notify(self.__direction)
