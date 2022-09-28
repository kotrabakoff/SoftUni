import abc

class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = int(fuel_quantity)
        self.fuel_consumption = int(fuel_consumption)

    def drive(self, kms):
        current_cosumption = self.fuel_consumption + 0.9
        if kms > self.fuel_quantity / current_cosumption:
            return
        self.fuel_quantity -= kms * current_cosumption

    def refuel(self, liters):
        self.fuel_quantity += liters

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = int(fuel_quantity)
        self.fuel_consumption = int(fuel_consumption)

    def drive(self, kms):
        current_consumption = self.fuel_consumption + 1.6
        if kms > self.fuel_quantity / current_consumption:
            return
        self.fuel_quantity -= kms * current_consumption

    def refuel(self, liters):
        self.fuel_quantity += liters * 95 / 100

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


