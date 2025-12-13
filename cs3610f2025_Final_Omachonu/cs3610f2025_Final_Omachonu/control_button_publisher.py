from subject import ISubject
from observer import IObserver

class ControlButtonPublisher(ISubject):
    def __init__(self) -> None:
        self.__observers: list[IObserver] = []

    def attach(self, observer: IObserver) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self, direction: str) -> None:
        for obs in self.__observers:
            obs.update(direction)
