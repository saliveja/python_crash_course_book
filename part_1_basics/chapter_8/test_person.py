import unittest
from person import Dictionary


class TestPerson(unittest.TestCase):
    """Making a test for person.py"""

    def setUp(self):
        """setting up the universal program attributes."""
        self.person = Dictionary('Anna', 'Andersson', 26)

    def test_parameters(self):
        """Testing so the information about a person
        is stored in a dictionary"""
        
        self.person.build_person()


if __name__ == '__main__':
    unittest.main()
