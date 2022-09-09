from project.vehicle import Vehicle

class Motorcycle(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)