from ICustomerBuilder import ICustomerBuilder
from CustomerClass import Customer



class CustomerDirector:

    def __init__(self):
        self._builder: ICustomerBuilder | None = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: ICustomerBuilder):
        self._builder = builder

    def constructCustomer(
        self,
        firstName: str,
        middleName: str | None,
        lastName: str,
        primaryEmail: str,
        secondaryEmail: str | None,
        primaryMobileNumber: str,
        secondaryMobileNumber: str | None,
    ):

        if self._builder is None:
            raise Exception("Director has no builder assigned.")

        self._builder.firstName(firstName)
        self._builder.middleName(middleName)
        self._builder.lastName(lastName)
        self._builder.primaryEmail(primaryEmail)
        self._builder.secondaryEmail(secondaryEmail)
        self._builder.primaryMobileNumber(primaryMobileNumber)
        self._builder.secondaryMobileNumber(secondaryMobileNumber)

        return self._builder.product
