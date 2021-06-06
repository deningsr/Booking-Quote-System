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
        elif (package.urgent == True) and ():
            return
