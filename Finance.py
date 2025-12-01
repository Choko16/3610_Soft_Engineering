# ---------- Adaptees (external modules we cannot change) ----------

class TaxCalculatorCSV:
    """
    Simulating an external tax calculator module.
    This module returns its result as a CSV string.
    """

    def get_tax_data_csv(self):
        # Example CSV output from the tax module
        return "year,income,tax_paid\n2024,50000,7500"


class AccountingModuleXML:
    """
    Simulated an external accounting module.
    This module returns its result as an XML string.
    """

    def get_accounting_data_xml(self):
        # Example XML output from the accounting module
        return "<accounting><year>2024</year><revenue>120000</revenue></accounting>"


class CreditAuthorizationJSON:
    """
    Simulates an external credit authorization service.
    This service already returns its result as JSON-style data.
    """

    def get_credit_data_json(self):
        # Example JSON-style output from the credit service
        return {
            "customer_id": 123,
            "credit_score": 720,
            "limit": 15000
        }


# ---------- Target interface (what the forecasting module expects) ----------

class FinancialDataSource:
    """
    Common interface for all financial data sources.
    The forecasting & finance modeling module expects any data source
    to provide data through this method in JSON-style format.
    """

    def get_data_as_json(self):
        # Subclasses must implement this method
        raise NotImplementedError("get_data_as_json() must be overridden by subclasses.")


# ---------- Adapters (object adapters using composition) ----------

class TaxCalculatorAdapter(FinancialDataSource):
    """
    Adapter for TaxCalculatorCSV.
    Converts the CSV output of the tax module into JSON-style data
    so that the forecasting module can work with it.
    """

    def __init__(self, adaptee):
        # Keep a reference to the external tax module (adaptee)
        self.__adaptee = adaptee

    def get_data_as_json(self):
        # Ask the tax module for its CSV result
        csv_data = self.__adaptee.get_tax_data_csv()

        # Wrap the CSV string into a dictionary so the client sees JSON-style data
        return {
            "source": "TaxCalculator",
            "format": "CSV",
            "raw_data": csv_data
        }


class AccountingModuleAdapter(FinancialDataSource):
    """
    Adapter for AccountingModuleXML.
    Converts the XML output of the accounting module into JSON-style data.
    """

    def __init__(self, adaptee):
        # Keep a reference to the external accounting module (adaptee)
        self.__adaptee = adaptee

    def get_data_as_json(self):
        # Ask the accounting module for its XML result
        xml_data = self.__adaptee.get_accounting_data_xml()

        # Wrap the XML string into a dictionary so the client sees JSON-style data
        return {
            "source": "AccountingModule",
            "format": "XML",
            "raw_data": xml_data
        }


class CreditAuthorizationAdapter(FinancialDataSource):
    """
    Adapter for CreditAuthorizationJSON.
    The credit service already returns JSON-style data, but we still use
    an adapter so that the forecasting module can treat all sources
    through the same interface (FinancialDataSource).
    """

    def __init__(self, adaptee):
        # Keep a reference to the external credit service (adaptee)
        self.__adaptee = adaptee

    def get_data_as_json(self):
        # Get the JSON-style data from the credit service
        data = self.__adaptee.get_credit_data_json()

        # Wrap it to keep a consistent structure with the other adapters
        return {
            "source": "CreditAuthorizationService",
            "format": "JSON",
            "data": data
        }


# ---------- Client (Forecasting & Finance Modeling Module) ----------

class ForecastingModule:
    """
    Simulates the forecasting & finance modeling module.
    This client only works with JSON-style dictionaries, not with CSV or XML.
    """

    def process_financial_data(self, data):
        """
        Receives JSON-style data from any FinancialDataSource implementation.
        In a real system, forecasting and analysis would be done here.
        For the assignment, we just print the data to show that
        the adapters are working.
        """
        print("Forecasting module received data:")
        print(data)
        print("Running analysis...\n")


# ---------- Client code / demonstration ----------

def client_code(data_source, forecasting_module):
    """
    Demonstrates that the client only depends on the FinancialDataSource
    interface. It does not need to know if the data came from CSV, XML,
    or JSON originally.
    """
    json_data = data_source.get_data_as_json()
    forecasting_module.process_financial_data(json_data)


if __name__ == "__main__":
    forecasting = ForecastingModule()

    # 1) Use the tax calculator module (CSV) through its adapter
    tax_calculator = TaxCalculatorCSV()
    tax_adapter = TaxCalculatorAdapter(tax_calculator)
    client_code(tax_adapter, forecasting)

    # 2) Use the accounting module (XML) through its adapter
    accounting_module = AccountingModuleXML()
    accounting_adapter = AccountingModuleAdapter(accounting_module)
    client_code(accounting_adapter, forecasting)

    # 3) Use the credit authorization service (JSON) through its adapter
    credit_service = CreditAuthorizationJSON()
    credit_adapter = CreditAuthorizationAdapter(credit_service)
    client_code(credit_adapter, forecasting)
