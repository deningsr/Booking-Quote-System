class Package:
    def __init__(self, customer_name, description, dangerous, weight, volume, del_date):
        self.customer_name = customer_name
        self.description = description
        self.dangerous = dangerous
        self.weight = weight
        self.volume = volume
        self.del_date = del_date


class BookingQuote:
    def __init__(self, package):
        self.package = package
