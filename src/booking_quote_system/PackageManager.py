class PackageManager:
    def __init__(self):

        """Initialized empty list of packages"""

        self.packages = []

    def new_package(self, package):

        """Creates a new package and adds it to the list"""

        self.packages.append(package)
