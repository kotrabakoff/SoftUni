from project.vehicle import Vehicle

from unittest import TestCase


class TestVehicle(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    KILOMETERS = 10
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init__(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test__drive__if_fuel_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test__drive__if_fuel_incremented(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        expected = self.FUEL - fuel_needed
        self.assertEqual(expected, self.vehicle.fuel)

    def test__drive__if_fuel_incremented_with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test__refuel__if_fuel_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertIsNotNone("Too much fuel", str(error.exception))

    def test__refuel__if_fuel_is_incremeted(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount
        self.vehicle.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test__str__if_string_is_same(self):
        to_test = str(self.vehicle)
        expected = f"The vehicle has {self.HORSE_POWER} " \
                   f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, to_test)

if __name__ == '__main__':
    unittest.main()