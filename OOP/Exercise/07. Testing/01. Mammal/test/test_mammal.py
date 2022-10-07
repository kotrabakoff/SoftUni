from project.mammal import Mammal

import unittest

class TestMammal(unittest.TestCase):
    NAME = "Gringo"
    TYPE = "Human"
    SOUND = "meh"

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test__init__(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)

    def test__make_sound__if_correct_string(self):
        expectation = f"{self.NAME} makes {self.SOUND}"
        to_test = self.mammal.make_sound()
        self.assertEqual(expectation, to_test)

    def test__get_kingdom__if_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test__info__if_correct_string(self):
        expected = f"{self.NAME} is of type {self.TYPE}"
        to_test = self.mammal.info()
        self.assertEqual(expected, to_test)

if __name__ == '__main__':
    unittest.main()
