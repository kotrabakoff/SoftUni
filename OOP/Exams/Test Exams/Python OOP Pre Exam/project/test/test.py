from project.movie import Movie
from unittest import TestCase

class MovieTests(TestCase):
    NAME = "Test Movie"
    YEAR = 1992
    RATING = 8.5
    MIN_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

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
            self.movie.year = self.MIN_YEAR - 10

        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor__append_when_name_does_not_exist(self):
        first = "Peshi"

        self.movie.add_actor(first)

        self.assertEqual([first], self.movie.actors)


    def test__add_actor__returns_error_for_duplicated_name(self):
        name = "Pesho"
        self.movie.actors = [name]

        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test__gt__expected_string_when_first_movie_has_greater_rating(self):
        another_movie_name = "Matrix"
        another_movie = Movie(another_movie_name, 1992, self.RATING - 1)

        first_result = self.movie > another_movie
        second_result = another_movie > self.movie

        expected_result = f'"{self.movie.name}" is better than "{another_movie_name}"'
        self.assertEqual(expected_result, first_result)
        self.assertEqual(expected_result, second_result)


    def test__repr__expected_result(self):
        actors = ['Pesho', 'Gosho']
        self.movie.actors = actors

        actual_result = repr(self.movie)
        expected_result = f"Name: {self.movie.name}\n" \
                          f"Year of Release: {self.movie.year}\n" \
                          f"Rating: {self.movie.rating:.2f}\n" \
                          f"Cast: {', '.join(self.movie.actors)}"

        self.assertEqual(actual_result, expected_result)