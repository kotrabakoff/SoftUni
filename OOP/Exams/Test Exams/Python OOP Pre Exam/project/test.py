from unittest import TestCase
from project.movie import Movie


class TestMovie(TestCase):
    NAME = "Test Movie"
    YEAR = 1992
    RATING = 8.5

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when_valid__exp_correct_values(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__name_setter__proper_raise_returned(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test__year_setter__proper_raise_returned(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = ''

        self.assertRaises("Year is not valid!", str(error.exception))
