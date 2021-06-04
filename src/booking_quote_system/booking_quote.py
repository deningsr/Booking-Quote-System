class Package:
    def __init__(self, cust_name, description, dangerous, weight, volume, del_date):
        self.cust_name = cust_name
        self.description = description
        self.dangerous = dangerous
        self.weight = weight
        self.volume = volume
        self.del_date = del_date


class BookingQuote:
    def __init__(self, package):
        self.package = package


class Customer:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Rule:
    def can_be_shipped(self, package):
        if package.weight < 10 or package.volume < 125:
            return True
        else:
            return False


class ShipmentMethod:
    pass
