import unittest
from city_functions import city_country


class CityCountryPopulationTestCase():
    """Testing city, country and population parameters."""

    def test_city_country_population(self):
        """Does it work with santiago, chile, population=5000000?"""
w
        city_country_population = city_country('santiago', 'chile',
                                               'population=5000000')
        self.assertEqual(city_country_population, 'santiago chile '
                                                  'population=5000000')


if __name__ == '__main__':
    unittest.main()
