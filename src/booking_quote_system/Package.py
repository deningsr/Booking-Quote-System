import uuid


class Package:
    def __init__(
        self,
        cust_fname,
        cust_lname,
        description,
        dangerous,
        weight,
        volume,
        del_date,
    ):
        self.package_id = str(uuid.uuid4().fields[-1])[:5]
        self.urgent = False
        self.cust_fname = cust_fname
        self.cust_lname = cust_lname
        self.description = description
        self.dangerous = dangerous
        self.weight = weight
        self.volume = volume
        self.del_date = del_date
        self.price_to_ship = 0

    def set_urgency(self):
        pass
