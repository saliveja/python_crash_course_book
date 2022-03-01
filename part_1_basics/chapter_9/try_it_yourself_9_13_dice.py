from random import randrange


class Dice():
    """printing random numbers."""

    def __init__(self, sides=6):
        """Initializing the dice class."""
        self.sides = sides
        # creating the parameter sides with default value 6

    def roll_die(self):
        """Rolling the die."""
        message = f"The die has {self.sides} sides. " \
                  f"Press enter to roll the die.\n" \
                  f"To quit press 'q'----->    "
        enter = input(message)
        x = int(self.sides) + 1
        # making the range 1, whatever argument is given for sides
        if enter == '':
            # if the user enters space, it returns a number
            range = randrange(1, x)
            return range
        elif enter.lower() == 'q':
            print("See you!")
            quit()
            # the user can quit the program by entering 'q'
            # a message is printed when choosing to exit
        else:
            print("Error. Try again.")
            quit()
            # if anything else than enter is

    def result(self):
        """Printing result"""
        res = self.roll_die()
        print(f"\nThe result is: {res}\n")
        # this method shows both roll_die() and results()
        # it prints the random number and the message


roll = Dice(10)
# die with six sides

while True:
    roll.result()
    # using a loop so the user can continue the
    # program for as long as they want

# roll = Dice(10)
# # dies with ten sides
# roll.result()
#
# roll = Dice(20)
# # die with twenty sides
# roll.result()
