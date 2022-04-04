import pygame
import random as random
from stars import Star


class EmptyScreen:

    def __init__(self, ):
        """Initializing empty screen."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 4000
        self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Stars")
        self.star = Star(self)
        self.stars = pygame.sprite.Group()
        self.create_star_grid()

    def run_program(self):
        """running the program."""
        while True:
            self.update_screen()

    def create_star_grid(self):
        """Drawing a grid of stars on the screen."""
        number = random.randrange(555, 1333)
        # making variable for the wished randomness of numbers

        for i in range(number):
            # for integer within the range defined in number
            x = random.randrange(
                self.screen_width - self.star.star_width)
            # Randomizing stars horizontally
            y = random.randrange(
                self.screen_height - self.star.star_height)
            # randomizing stars vertically
            self.create_star(x, y)
            # calling for the method create_star with the randomization
            # defined above

    def create_star(self, x, y):
        """Create star and place in the grid."""
        star = Star(self)
        # making an instance of class Star
        star.rect.x = x
        # rect us used to store and manipulate rectangular areas
        # most of the information comes from the class Stars
        # here, we get access to the horizontal rect
        star.rect.y = y
        # accessing vertical rect
        # we wanted to randomize on x and y-axis
        # we also need access to position the stars on both axis
        # these two variables gives access to these two rect

        self.stars.add(star)
        # adding star to the group stars from the class Star

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.stars.update()
        # self.create_star_grid()
        pygame.display.flip()


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
