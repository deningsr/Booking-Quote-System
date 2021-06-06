from datetime import datetime
import sys
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


class PackageManager:
    def __init__(self):

        """Initialized empty list of packages"""

        self.packages = []

    def new_package(self, package):

        """Creates a new package and adds it to the list"""

        self.packages.append(package)


class BookingQuote:
    def __init__(self, package):
        self.package = package


class Customer:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Rules:
    def ship_via_air(self, package):
        if (
            (package.weight < 10)
            and (package.volume < 125)
            and (package.dangerous == False)
        ):
            print("Your package will be routed via air!")
            price_per_kg = package.weight * 10
            price_per_cubic_meter = package.weight * 20
            if price_per_kg > price_per_cubic_meter:
                package.price_to_ship = price_per_kg
            else:
                package.price_to_ship = price_per_cubic_meter
            package.price_to_ship = 
        else:
            return False

    def ship_via_truck(self):
        pass


class Menu:

    """Displays a list of options on the terminal for the user to run"""

    def __init__(self):
        self.packages = PackageManager()

        self.choices = {
            "1": self.ship_package,
            "2": self.save_package,
            "3": self.show_all_packages,
            "4": self.quit,
        }

    def display_menu(self):
        print(
            """
        
               Booking Quote System Menu

               1.  Ship a package

               2.  Save package to CSV

               3.  Display all packages

               4.  Quit Program
            """
        )

    def run(self):
        """Displays menu and respond to user inputs"""

        while True:
            self.display_menu()

            choice = input("Please enter an option below: ")

            response = self.choices.get(choice)

            if response:
                response()
            else:
                print("{0} is not a valid choice".format(choice))

    def ship_package(self):
        """Ships a new package and adds it to the list"""

        cust_fname = input("Enter First Name: ")
        cust_lname = input("Enter Last Name: ")
        description = input("Enter package description: ")
        dangerous = input("Are the contents dangerous (True/False)?: ")
        weight = input("Enter package weight in kg: ")
        volume = input("Enter package volume in cubic meters: ")
        del_date = input("Enter required package delivery date: ")

        package_to_ship = Package(
            cust_fname,
            cust_lname,
            description,
            dangerous,
            weight,
            volume,
            del_date,
        )

        Rules.ship_via_air(package_to_ship)

        self.packages.new_package(package_to_ship)

    def quit(self):
        """quits or terminates the program"""

        print("Thank you for using the Booking Quote System")

        sys.exit(0)


if __name__ == "__main__":

    Menu().run()
