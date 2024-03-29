class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25
    fuel_consumption = float()
    fuel = float()
    horse_power = int()

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        previous_fuel = self.fuel
        self.fuel -= kilometers * self.fuel_consumption
        if self.fuel < 0:
            self.fuel = previous_fuel
            return self.fuel
        return self.fuel




