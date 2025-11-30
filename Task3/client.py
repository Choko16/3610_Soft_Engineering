from CustomerDirector import CustomerDirector
from WebAppCustomerBuilder import WebAppCustomerBuilder
from MobileAppCustomerBuilder import MobileAppCustomerBuilder


def run_demo():
    director = CustomerDirector()

    print("From Web Application (all fields):")
    web_builder = WebAppCustomerBuilder()
    director.builder = web_builder

    c1 = director.constructCustomer(
        firstName="Emeka",
        middleName="obioma",
        lastName="John",
        primaryEmail="emeka@gmail.com",
        secondaryEmail="john.e@gmail.com",
        primaryMobileNumber="123-456-8934",
        secondaryMobileNumber="987-765-4321",
    )
    c1.showComponents()

    print("From Mobile Application (mandatory fields only):")
    mobile_builder = MobileAppCustomerBuilder()
    director.builder = mobile_builder

    c2 = director.constructCustomer(
        firstName="clinton",
        middleName=None,
        lastName="owusu",
        primaryEmail="owusu@gmails.com",
        secondaryEmail=None,
        primaryMobileNumber="123-456-8934",
        secondaryMobileNumber=None,
    )
    c2.showComponents()


if __name__ == "__main__":
    run_demo()
