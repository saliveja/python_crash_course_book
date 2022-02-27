from random import randrange


class Dice():
    """printing random numbers."""

    def __init__(self, sides=6):
        """Initializing the dice class."""
        self.sides = sides
        # creating the parameter sides with default value

    def roll_die(self):
        """Rolling the die."""
        message = f"The die has {self.sides} sides. " \
                  f"Press enter to roll the die"
        enter = input(message)
        x = int(self.sides) + 1
        # making the range 1, whatever argument is given for sides
        if enter == '':
            # if the user enters space, it returns a number
            range = randrange(1, x)
            return range
        else:
            print("no")
            quit()

    def result(self):
        """Printing result"""
        res = self.roll_die()
        print(f"The result is: {res}")
        # this method shows both roll_die() and results()
        # it prints the random number and the message


roll = Dice(6)
# die with six sides
roll.result()

roll = Dice(10)
# dies with ten sides
roll.result()

roll = Dice(20)
# die with twenty sides
roll.result()
