from project.hero import Hero

from unittest import TestCase

class TestHero(TestCase):
    USERNAME = "kotrabakoff"
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 20

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__init__(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test__battle__fighting_himself_exception(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test__batle__health_lower_equal_0(self):
        current_hero = Hero(self.USERNAME, self.LEVEL, 0, self.DAMAGE)
        opponent = Hero("Ivan", 8, 90, 15)
        with self.assertRaises(ValueError) as error:
            current_hero.battle(opponent)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))


    def test__battle__if_enemy_helth_lower_equal_0(self):
        opponent = Hero("Ivan", 8, 0, 15)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(opponent)
        self.assertEqual(f"You cannot fight Ivan. He needs to rest", str(error.exception))

    def test__battle__if_damage_calculates_properly(self):
        opponent = Hero("Ivan", 8, 90, 15)
        hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        my_damage = self.DAMAGE * self.LEVEL
        opponent_damage = opponent.damage * opponent.level
        self.assertEqual(my_damage, hero.damage * hero.level)
        self.assertEqual(opponent_damage, opponent.damage * opponent.level)

    def test__battle__after_fight_any_health_equal_less_0(self):
        opponent = Hero("Ivan", self.LEVEL, self.HEALTH, self.DAMAGE)
        result = self.hero.battle(opponent)
        expected_health = self.HEALTH - self.DAMAGE * self.LEVEL
        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, opponent.health)

    def test__battle__if_i_win(self):
        opponent = Hero("Ivan", 8, 10, 5)
        result = self.hero.battle(opponent)
        my_health = self.HEALTH - opponent.damage * opponent.level
        self.LEVEL += 1
        self.HEALTH += 5
        self.DAMAGE += 5
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(65, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)
        self.assertEqual("You win", result)


    def test__battle__if_i_lose(self):
        hero = Hero("kotrabakoff", 10, 4, 2)
        opponent = Hero("Ivan", 200, 300, 500)
        result = self.hero.battle(opponent)
        opponent.health -= hero.damage * hero.level
        self.assertEqual(201, opponent.level)
        self.assertEqual(85, opponent.health)
        self.assertEqual(505, opponent.damage)
        self.assertEqual("You lose", result)



    def test__str__(self):
        expected = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"
        test = str(self.hero)
        self.assertEqual(test, expected)


