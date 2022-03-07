import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    # it's helpful to use the word Test when naming the class
    # the class inherits from unittest.Testcase

    def test_first_last_name(self):
        """Do names like Janis Joplin work?"""

        formatted_name = get_formatted_name('janis', 'joplin')
        # calling th function we want to test
        self.assertEqual(formatted_name, 'Janis Joplin')
        # assertEqual() is a unittest method to verify that
        # the received result matches expected result -->
        # comparing the value in formatted_name with 'Janis Joplin'


if __name__ == '__main__':
    unittest.main()
# when running test --> a dot on the first line means that a
# single test passed
