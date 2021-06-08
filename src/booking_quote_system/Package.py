import uuid
import datetime


def set_urgency(del_date):
    now = datetime.datetime.now()
    urgent_date = now + datetime.timedelta(days=3)
    return datetime.datetime.strptime(del_date, "%m-%d-%Y") < urgent_date


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
        self.urgent = set_urgency(del_date)
        self.cust_fname = cust_fname
        self.cust_lname = cust_lname
        self.description = description
        self.dangerous = dangerous
        self.weight = weight
        self.volume = volume
        self.del_date = datetime.datetime.strptime(del_date, "%m-%d-%Y")
        self.price_to_ship = 0
