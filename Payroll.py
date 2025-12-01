from abc import ABC, abstractmethod

# -------------------------------------------------------
# Implementor side of the Bridge: payment processing
# -------------------------------------------------------

class IPaymentProcessor(ABC):
    """
    Common interface for anything that can send money to an employee.
    In the Bridge pattern this is the Implementor.
    """

    @abstractmethod
    def pay(self, employee_name: str, amount: float) -> str:
        """
        Do the actual transfer of money and return
        a short message describing what happened.
        """
        pass

    def __str__(self) -> str:
        # Same idea as in the lecture examples: show the class name
        return f"{self.__class__}"


class BankTransferProcessor(IPaymentProcessor):
    """
    Concrete payment processor that represents a bank transfer.
    """

    def pay(self, employee_name: str, amount: float) -> str:
        return f"[BankTransfer] Paying {employee_name} ${amount:.2f} via bank transfer."


class ChequeProcessor(IPaymentProcessor):
    """
    Concrete payment processor that represents a cheque payment.
    """

    def pay(self, employee_name: str, amount: float) -> str:
        return f"[Cheque] Paying {employee_name} ${amount:.2f} via cheque."


class DigitalWalletProcessor(IPaymentProcessor):
    """
    Concrete payment processor that represents a digital wallet transfer.
    """

    def pay(self, employee_name: str, amount: float) -> str:
        return f"[DigitalWallet] Paying {employee_name} ${amount:.2f} to digital wallet."


# Map from a simple string name to the corresponding payment class.
# This is the same pattern used in the Factory Method examples.
myPaymentMethods = {
    "BankTransfer": BankTransferProcessor,
    "Cheque": ChequeProcessor,
    "DigitalWallet": DigitalWalletProcessor,
}


class PaymentCreator:
    """
    Factory Method class.
    It centralizes the logic for creating a payment processor
    from a text value like "Cheque" or "BankTransfer".
    """

    @staticmethod
    def create_payment(method_type: str) -> IPaymentProcessor:
        """
        Factory Method:
        - method_type is a string used as a key in myPaymentMethods.
        - if the key exists, build and return the correct processor.
        """
        try:
            if method_type in myPaymentMethods.keys():
                return myPaymentMethods[method_type]()
            else:
                raise Exception("Unknown payment method type.")
        except Exception as _e:
            print(_e)
        return None


# -------------------------------------------------------
# Abstraction side of the Bridge: employee hierarchy
# -------------------------------------------------------

class IEmployee(ABC):
    """
    Base class for all employees.

    This is the Abstraction in the Bridge pattern.
    Each employee:
    - has a name
    - keeps a reference to a payment processor (Implementor)
    """

    def __init__(self, name: str, payment_processor: IPaymentProcessor) -> None:
        self._name = name
        self._payment_processor = payment_processor

    @abstractmethod
    def calculate_salary(self) -> float:
        """
        Each concrete employee type has its own way
        to compute the amount it should be paid.
        """
        pass

    def process_payment(self) -> str:
        """
        High-level operation:
        1) Ask the subclass for the salary amount.
        2) Delegate the actual payment to the payment processor.
        """
        amount = self.calculate_salary()
        return self._payment_processor.pay(self._name, amount)


class HourlyEmployee(IEmployee):
    """
    Employee paid by the hour.
    Salary formula: hours_worked * hourly_rate
    """

    def __init__(
        self,
        name: str,
        hours_worked: float,
        hourly_rate: float,
        payment_processor: IPaymentProcessor,
    ) -> None:
        super().__init__(name, payment_processor)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def calculate_salary(self) -> float:
        return self.__hours_worked * self.__hourly_rate


class SalariedEmployee(IEmployee):
    """
    Employee with a fixed monthly salary.
    """

    def __init__(
        self,
        name: str,
        monthly_salary: float,
        payment_processor: IPaymentProcessor,
    ) -> None:
        super().__init__(name, payment_processor)
        self.__monthly_salary = monthly_salary

    def calculate_salary(self) -> float:
        return self.__monthly_salary


class ContractorEmployee(IEmployee):
    """
    Contractor paid a fixed fee for a project.
    """

    def __init__(
        self,
        name: str,
        project_fee: float,
        payment_processor: IPaymentProcessor,
    ) -> None:
        super().__init__(name, payment_processor)
        self.__project_fee = project_fee

    def calculate_salary(self) -> float:
        return self.__project_fee


# -------------------------------------------------------
# Application / client code to demonstrate the design
# -------------------------------------------------------

class PayrollApp:
    """
    Small driver class to demonstrate the Bridge + Factory Method solution.

    - AvalPaymentMethods shows which payment methods are supported.
    - run_demo() creates payment processors using the factory,
      creates some example employees and triggers their payments.
    """

    def __init__(self) -> None:
        # Property listing all available payment methods by name.
        self.AvalPaymentMethods = ["BankTransfer", "Cheque", "DigitalWallet"]

    def run_demo(self) -> None:
        # 1. Create the payment processors using the Factory Method.
        bank_transfer = PaymentCreator.create_payment("BankTransfer")
        cheque = PaymentCreator.create_payment("Cheque")
        digital_wallet = PaymentCreator.create_payment("DigitalWallet")

        employees = []

        # 2. For each processor, create one employee that uses it.
        #    This is where the Bridge is visible: each employee is
        #    linked to a specific IPaymentProcessor object.
        if bank_transfer:
            salaried = SalariedEmployee("Sam Salary", 5000.0, bank_transfer)
            employees.append(salaried)

        if cheque:
            hourly = HourlyEmployee("Hanna Hourly", 160, 25.0, cheque)
            employees.append(hourly)

        if digital_wallet:
            contractor = ContractorEmployee("Choko Contract", 8000.0, digital_wallet)
            employees.append(contractor)

        # 3. Ask each employee to process its own payment.
        for emp in employees:
            result = emp.process_payment()
            print(result)


# -------------------------------------------------------
# Client entry point
# -------------------------------------------------------

if __name__ == "__main__":
    app = PayrollApp()
    app.run_demo()
