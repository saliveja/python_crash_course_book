class Lottery():
    """Making a lottery."""

    def __init__(self, numbers, letters):
        """Initializing lottery."""
        self.numbers = numbers
        self.letters = letters

    def randomized_selection(self):
        """Selecting the winners."""
        selection = randrange(lottery)

    def message_to_winner(self):
        """Printing a message to the winners."""
        print("Any ticket that matches these numbers or letters, "
              "win a trip to Iceland:\n")
        print(f"{self.numbers} {self.letters}")


lottery = ['1', '2', '3', '4', '5',
           '6', '7', '8', '9', '10',
           'a', 'b', 'c', 'd', 'e']