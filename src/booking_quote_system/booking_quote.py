from datetime import datetime
import sys


class Package:
    price_to_ship = 0

    def __init__(self, cust_name, description, dangerous, weight, volume, del_date):
        self.urgent = False
        self.cust_name = cust_name
        self.description = description
        self.dangerous = dangerous
        self.weight = weight
        self.volume = volume
        self.del_date = del_date

    def set_urgency(self):
        pass


class PackageManager:
    def __init__(self):

        """Initialized empty list of packages"""

        self.packages = []

    def new_package(self, cust_name, description, dangerous, weight, volume, del_date):

        """Creates a new package and adds it to the list"""

        self.packages.append(
            Package(cust_name, description, dangerous, weight, volume, del_date)
        )


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
            return True
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

    def quit(self):
        """quits or terminates the program"""

        print("Thank you for using the Booking Quote System")

        sys.exit(0)
