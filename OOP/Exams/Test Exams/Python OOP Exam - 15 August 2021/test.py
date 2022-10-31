from unittest import TestCase

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    NAME = "Paws"

    def setUp(self) -> None:
        self.petshop = PetShop(self.NAME)

    def test__init(self):
        self.assertEqual(self.NAME, self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test__add_food__if_error_raise(self):
        with self.assertRaises(ValueError) as error:
            self.petshop.add_food("Granules", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.valueerror)
