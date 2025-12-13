from abc import ABC, abstractmethod
from observer import IObserver

class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify(self, direction: str) -> None:
        pass
