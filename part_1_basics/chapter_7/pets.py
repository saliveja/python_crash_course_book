# using remove() to remove all instances of value from a list

class NoRepetition:
    """Making a class to remove an item from a list."""

    def __init__(self, all_items, item):
        self.all_items = all_items
        self.item = item

    def poppingItem(self):
        """Removing specific items from a list."""

        while self.item in self.all_items:
            self.all_items.remove(self.item)
            # using the while loop to delete all 'cat' values in the list
            # the loop ensures that the loop continues until all 'cat'
            # are removed

    def printPoppedItem(self):
        """Printing the item that was popped."""
        print(f"This is the removed item: {self.item}")
