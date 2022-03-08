import unittest
from pets import NoRepetition


class TestNoRepetition(unittest.TestCase):
    """Testing class NoRepetition."""

    def setUp(self):
        pet_list = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
        remove_animal = 'cat'
        self.repetition = NoRepetition(pet_list, remove_animal)

    def testPoppingItem(self):
        """Testing method PoppedItem."""
        self.repetition.poppingItem()

    def testPrintPoppedItem(self):
        """Testing method printPoppedItem."""
        self.repetition.printPoppedItem()


if __name__ == '__main__':
    unittest.main()
