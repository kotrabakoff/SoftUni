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
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test__add_food__if_error_raised(self):
        with self.assertRaises(ValueError) as error:
            self.petshop.add_food("Granules", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test__add_food__if_name_not_in_food(self):
        food_added = self.petshop.add_food("Granules", 200)
        self.assertEqual(200, self.petshop.food["Granules"])
        expected = "Successfully added 200.00 grams of Granules."
        self.assertEqual(expected, food_added)


    def test__add_food__if_it_adds_properly(self):
        self.petshop.add_food("Granules", 200)
        food_added = self.petshop.add_food("Granules", 200)
        self.assertEqual(400, self.petshop.food["Granules"])
        expected = "Successfully added 200.00 grams of Granules."
        self.assertEqual(expected, food_added)

    def test__add_pet__if_not_in_pets_list(self):
        pet_added = self.petshop.add_pet("Tommy")
        self.assertEqual(["Tommy"], self.petshop.pets)
        self.assertEqual("Successfully added Tommy.", pet_added)

    def test__add_pet__if_in_pets_list(self):
        self.petshop.add_pet("Tommy")
        with self.assertRaises(Exception) as error:
            self.petshop.add_pet("Tommy")
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test__feed_pet__if_pet_not_in_list(self):
        with self.assertRaises(Exception) as error:
            self.petshop.feed_pet("Granules", "Tommy")
        self.assertEqual("Please insert a valid pet name", str(error.exception))

    def test__feed_pet__if_pet_not_in_list(self):
        self.petshop.add_pet("Tommy")
        pet_fed = self.petshop.feed_pet("CatFood", "Tommy")
        self.assertEqual('You do not have CatFood', pet_fed)

    def test__feed_pet__if_quntity_below_100(self):
        self.petshop.add_food("Granules", 50)
        self.petshop.add_pet("Tommy")
        pet_fed = self.petshop.feed_pet("Granules", "Tommy")
        self.assertEqual(1050, self.petshop.food["Granules"])
        self.assertEqual("Adding food...", pet_fed)

    def test__feed_pet__if_quntity_above_100(self):
        self.petshop.add_food("Granules", 120)
        self.petshop.add_pet("Tommy")
        pet_fed = self.petshop.feed_pet("Granules", "Tommy")
        self.assertEqual(20, self.petshop.food["Granules"])
        self.assertEqual("Tommy was successfully fed", pet_fed)

    def test__repr__if_properly_returned(self):
        self.petshop.add_food("Granules", 120)
        self.petshop.add_pet("Tommy")
        self.petshop.add_pet("Jerry")
        expected = f'Shop Paws:\n' \
                   f'Pets: Tommy, Jerry'
        self.assertEqual(expected, str(self.petshop))




