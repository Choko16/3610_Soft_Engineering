from ICustomerBuilder import ICustomerBuilder
from CustomerClass import Customer

class MobileAppCustomerBuilder(ICustomerBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Customer()

    @property
    def product(self):
        finished = self._product
        self.reset()
        return finished

    
    def firstName(self, value: str):
        self._product.add("firstName", value)

    def middleName(self, value: str | None):
        pass  

    def lastName(self, value: str):
        self._product.add("lastName", value)

    def primaryEmail(self, value: str):
        self._product.add("primaryEmail", value)

    def secondaryEmail(self, value: str | None):
        pass  

    def primaryMobileNumber(self, value: str):
        self._product.add("primaryMobileNumber", value)

    def secondaryMobileNumber(self, value: str | None):
        pass  
