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

        the_chosen_number = input(prompt)
        # The reponse to the prompt is the chosen number
        print(f"You have chosen the number {the_chosen_number} for "
              f"the lottery draw.")
        self.ticket = int(the_chosen_number)
        return self.ticket

        # printing the chosen number

    def randomized_number(self):
        """ The lottery draw."""
        lottery_draw = randrange(1, 801)
        number_of_loops = 0

        while lottery_draw != self.ticket:
            number_of_loops += 1
            print(f"the draw number {number_of_loops} is"
                  f" ===== {lottery_draw}")
            lottery_draw = randrange(1, 801)

        print(f"Congratulation!! Number {self.ticket} is the winner.")
        print(f"It took {number_of_loops} draws before you won.")


# retries = 0
#
# def random_numbers(self):
#     prompt = "Write the number you want to use for the lottery."
#     my_number_1 = input(prompt)
#     my_number_2 = input("You can choose one more number "
#                         "for the lottery. ")
#
#     tickets = []
#
#     for x in range(800):
#         tickets.append(my_number_1)
#         tickets.append(my_number_2)
#
#
#     if x == ticket:
#         number_of_loops += 1
#
#
#     else:
#         for items in tickets:
#             print("Lotto number {}".format(item))
#             lotto_number += 1
#         print("The number of tries", retries)


check_number = Looping_numbers()
check_number.ticket_number()
check_number.randomized_number()
