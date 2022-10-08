# [ ] Finish task
# [ ] Save files to drive

# Create class Vehicle which contains necessary information about car/bus/motorcycle (up to you).
# Create method that computes the maximum reachable distance based on the volume of the fuel tank
# and the argument of the function of `average_fuel_consumption`
# Create this class in separate module and import it into the main file and try it with average fuel consumption of
# 5l/100km and 7.3l/100km

class Vehicle:
    def __init__(self, name, tank_capacity):
        self.name = name
        self.tank_capacity = tank_capacity

    def max_reachable_distance(self, average_fuel_consumption):
        max_distance = 100/average_fuel_consumption/(self.tank_capacity)
        return print(self.name, "can go maximum", max_distance, "km")

car = Vehicle("Ferrari",78)
car.max_reachable_distance(5))
car.max_reachable_distance(7.3)