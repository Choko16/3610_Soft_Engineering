
class Customer:
    def __init__(self) -> None:
        self.__name = "Customer"
        self.__components = []   # holds all fields as components

    def add(self, componentName: str, value) -> None:
        """Adds a field-value pair as a component of the product."""
        print(f"Adding {componentName}: {value}")
        self.__components.append((componentName, value))

    def showComponents(self) -> None:
        print(f"There are {len(self.__components)} component(s) in this {self.__name}.")
        print(f"The components of this {self.__name} are:")
        for fieldName, fieldValue in self.__components:
            print(f"  {fieldName}: {fieldValue}")
        print("-" * 40)
