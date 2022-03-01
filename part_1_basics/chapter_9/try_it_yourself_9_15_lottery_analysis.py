from random import randrange


class Looping_numbers():
    """This class is for looping through numbers in a lottery."""

    def __init__(self):
        """Initializing"""

    def ticket_number(self):
        """Choosing a number for the lottery."""
        lottery_range = list(range(801))
        prompt = "Write the number you want to use for the lottery."
        # making a prompt for user to choose a number for the lottery draw.
        prompt += f"You can choose a number between {lottery_range[0]} " \
                  f"and {lottery_range[-1]}."
        # using list index to specify that the number can only be
        # chosen between 1 and 800

        the_chosen_number = input(prompt)
        # The response to the prompt is the chosen number
        print(f"You have chosen the number {the_chosen_number} for "
              f"the lottery draw.")
        self.ticket = int(the_chosen_number)
        # defining the number as an integer and making if usable
        # in all methods in the class

    def randomized_number(self):
        """ The lottery draw."""
        lottery_draw = randrange(1, 801)
        # making a variable of randrange
        # randrange will select a number between 1 and 801
        number_of_loops = 0
        # default number of loops/starting point is set to zero

        while lottery_draw != self.ticket:
            # while the number in randrange is not the chosen number
            number_of_loops += 1
            # add 1 for every new loop
            # the counting of loops increases
            print(f"the draw number {number_of_loops} is"
                  f" ===== {lottery_draw}")
            lottery_draw = randrange(1, 801)
            # drawing the number

        print(f"Congratulation!! Number {self.ticket} is the winner.")
        # when the number that i drawn matches the chosen number,
        # this message is printed
        print(f"It took {number_of_loops} draws before you won.")
        # prints how many draws were needed before the chosen number
        # was the winning number


check_number = Looping_numbers()
check_number.ticket_number()
check_number.randomized_number()
