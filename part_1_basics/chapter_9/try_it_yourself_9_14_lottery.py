from string import ascii_lowercase
from random import randrange
from random import sample


class Lottery():
    """Making a lottery."""

    def __init__(self):
        """Initializing lottery."""

    def make_lottery_list(self):
        """Making the list of numbers."""
        lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8',
                        '9', '10', 'a', 'b', 'c', 'd', 'e']
        self.list = lottery_list

        print(f"The following tickets have the possibility of "
              f"winning todays lottery: {self.list}")

    def selection_from_list(self):
        """Making a selection from the list."""
        desired_number = 4
        randomized_selection = sample(self.list, desired_number)
        self.selection = randomized_selection

    # def message_to_winner(self):
    #     """Printing a message to the winners."""
    #     message = "Press enter to see the four winners "
    #     enter = input(message)
    #     if enter == '':
    #         print(f"{self.selection}")
    #         print("Congratulation, you are one of the lucky winners!!"
    #               " You and another person will travel to Iceland for "
    #               "a weekend.")

#
# x = Lottery()
# x.make_lottery_list()
# x.selection_from_list()
# # x.message_to_winner()
