import unittest
import try_it_yourself_17_1_other_languages as ol


class CheckValue(unittest.Testcase):
    """test for try_it_yourself_17_1_other_languages.py"""

    def __init__(self):
        """Initializing test class"""

    def test_status_code(self):
        """Asserting value of status code to 200"""

        self.assertEqual(ol.r.status_code, 200)

    def test_number_of_items(self):
        """Testing if the number items are as expected"""
        self.assertEqual(ol.repo_dicts, 30)

    def testing_number_of_repositories(self):
        """Testing so the number of repositories are greater
        than a certain amount"""
        self.assertEqual(ol.total_count, 994678)


if __name__ == '__main__':
    unittest.main()
