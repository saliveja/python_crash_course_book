import pygame
import random as random
from raindrops import Rain


class Rain:

    def __init__(self):
        """Initializing the program."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 4000
        self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Rain")
        self.rain = Rain(self)
        self.rain_fall = pygame.sprite.Group()
        self.create_raindrop()

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
                self.screen_width - self.rain.star_width)
            # Randomizing stars horizontally
            y = random.randrange(
                self.screen_height - self.rain.star_height)
            # randomizing stars vertically
            self.create_raindrop(x, y)
            # calling for the method create_star with the randomization
            # defined above

    def create_raindrop(self, x, y):
        """Create an alien and place it in the row."""
        rain = Rain(self)
        # making an instance of class Star
        rain.rect.x = x
        # rect us used to store and manipulate rectangular areas
        # most of the information comes from the class Stars
        # here, we get access to the horizontal rect
        rain.rect.y = y
        # accessing vertical rect
        # we wanted to randomize on x and y-axis
        # we also need access to position the stars on both axis
        # these two variables gives access to these two rect

        self.rain_fall.add(rain)
        # adding star to the group stars from the class Star

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.rain.update()
        # self.create_star_grid()
        pygame.display.flip()


if __name__ == '__main__':
    rain = Rain()
    rain.run_program()
