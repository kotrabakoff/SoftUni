from project.motorcycle import Motorcycle

class Crossmotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)



