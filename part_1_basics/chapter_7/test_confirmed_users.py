import unittest
from confirmed_users import Users


class TestUsers(unittest.TestCase):
    """Tests for the class Users."""

    def setUp(self):
        x = ['hanna', 'karl', 'greta']
        empty = []
        self.users = Users('Anna', empty, x)

    def testPop(self):
        self.users.poppingUser()

    def testverify(self):
        """Testing printing of verifies users."""
        self.users.verifyingUser()

    def testPrint(self):
        self.users.printUsers()


if __name__ == '__main__':
    unittest.main()
