import unittest
from city_functions import city_country


class CityCountryTestcase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Does city/country like Oslo, Norway work?"""

        name_city_country = city_country('oslo', 'norway')
        self.assertEqual(name_city_country, 'Oslo Norway')


if __name__ == '__main__':
    unittest.main()
