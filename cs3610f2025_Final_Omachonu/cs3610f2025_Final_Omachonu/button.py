class Button:
    def __init__(self, label: str) -> None:
        self._label = label

    @property
    def label(self) -> str:
        return self._label

    def set_label(self, new_label: str) -> None:
        self._label = new_label

    def click(self) -> None:
        # Subclasses decide what click does
        pass
