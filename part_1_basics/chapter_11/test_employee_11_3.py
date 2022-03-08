import unittest
from try_it_yourself_11_3_employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        self.employee = Employee('Anna', 'Andersson', 8000)
    
    def test_give_default_raise(self):
        """This is testing that the default
        raise is working properly."""

        self.employee.give_raise()

    def test_give_custom_raise(self):
        """This is testing that the custom raise
        option is working properly."""
        self.amount = 8000
        self.employee.give_raise()


if __name__ == '__main__':
    unittest.main()
