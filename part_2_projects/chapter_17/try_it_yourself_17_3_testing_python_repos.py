import unittest
import requests as r
import try_it_yourself_17_1_other_languages as ol


class CheckValue(unittest.TestCase):
    """test for try_it_yourself_17_1_other_languages.py"""

    def test_status_code(self):
        """Asserting value of status code to 200"""
        status_code = ol.r.status_code
        self.assertEqual(status_code, 200)

    def test_number_of_items(self):
        """Testing if the number keys are as expected"""
        self.assertEqual(ol.keys, 78)

    def testing_number_of_repositories(self):
        """Testing so the number of repositories are greater
        than a certain amount"""
        repos = len(ol.repo_dict)
        self.assertTrue(repos < 992000)


if __name__ == '__main__':
    unittest.main()
