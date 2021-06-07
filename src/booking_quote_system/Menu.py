import sys
import csv
from datetime import datetime
from booking_quote_system.Package import Package
from booking_quote_system.PackageManager import PackageManager


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
        self.create_initial_file()
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

        # Rules.ship_via_air(self, package_to_ship)

        self.packages.new_package(package_to_ship)

    def create_initial_file(self):
        with open("booking_quotes.csv", "w") as file:
            fieldnames = [
                "cust_fname",
                "cust_lname",
                "dangerous",
                "del_date",
                "description",
                "package_id",
                "price_to_ship",
                "urgent",
                "volume",
                "weight",
            ]
            dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
            dict_writer.writeheader()

    def save_package(self):
        packages = self.packages.packages
        with open("booking_quotes.csv", "a", newline="") as file:
            # for package in packages:
            #     members = [
            #         attr
            #         for attr in dir(package)
            #         if not callable(getattr(package, attr))
            #         and not attr.startswith("__")
            #     ]
            #     values = [getattr(package, member) for member in members]
            #     readData = dict(zip(members, values))
            #     dict_writer = csv.DictWriter(file, fieldnames=members)
            #     dict_writer.writeheader()
            #     dict_writer.writerow(readData)

            members = [
                attr
                for attr in dir(packages[-1])
                if not callable(getattr(packages[-1], attr))
                and not attr.startswith("__")
            ]
            values = [getattr(packages[-1], member) for member in members]
            readData = dict(zip(members, values))
            dict_writer = csv.DictWriter(file, fieldnames=members)
            # dict_writer.writeheader()
            dict_writer.writerow(readData)

    def show_all_packages(self):
        for package in self.packages.packages:
            members = [
                attr
                for attr in dir(package)
                if not callable(getattr(package, attr)) and not attr.startswith("__")
            ]
            print(members)
            print([getattr(package, member) for member in members])

    def quit(self):
        """quits or terminates the program"""

        print("Thank you for using the Booking Quote System")

        sys.exit(0)


if __name__ == "__main__":

    Menu().run()
