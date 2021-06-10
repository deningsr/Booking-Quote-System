def determine_shipping(package):
    cost_by_air_weight = package.weight * 10
    cost_by_air_volume = package.volume * 20
    cost_by_truck = 25
    cost_by_truck_if_urgent = 45
    cost_by_sea = 30
    if (package.dangerous == False) and (package.urgent == True):
        package.price_to_ship = max(cost_by_air_volume, cost_by_air_weight)
        print("Your package will be routed via air!")
    # if package.urgent == True:
    #     print("Your package will be delivered within 3 business days")
    #     price_per_kg = package.weight * 10
    #     price_per_cubic_meter = package.weight * 20
    #     if price_per_kg > price_per_cubic_meter:
    #         package.price_to_ship = price_per_kg
    #     else:
    #         package.price_to_ship = price_per_cubic_meter
    # elif (package.urgent == True) and ():
    #     return

    return package
