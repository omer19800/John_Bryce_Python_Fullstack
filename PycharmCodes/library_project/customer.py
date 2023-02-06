import address
import dates

class Customer:

    def __init__(self, id: int, name: str, address, email, birthday):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.birthday = birthday


        # address - diffrent class to confirm all details correct
        #birthday - diffrent class to work with datetime module