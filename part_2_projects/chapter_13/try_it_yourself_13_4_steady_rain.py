import sys
import pygame
import random
from raindrops import Raindrop


class FallingRain:

    def __init__(self):
        """Initializing the program."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        # self.screen_width = 4000
        # self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("Falling rain")
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.raindrop = Raindrop(self)
        self.rain_fall = pygame.sprite.Group()
        self.create_rain_grid()

    def run_program(self):
        """running the program."""
        while True:
            self.check_key_event()
            self.update_position()
            self.update_screen()

    def create_rain_grid(self):
        """Drawing a grid of raindrops on the screen."""
        number = random.randrange(50, 70)

        raindrop_width, raindrop_height = self.raindrop.rect.size

        for i in range(number):
            x = random.randrange(
                self.screen_width - raindrop_width)
            y = random.randrange(
                self.screen_height - raindrop_height) - self.screen_height

            self.create_raindrop(x, y)

    def new_raindrop(self):

        """Creates new raindrop on top of the screen"""
        raindrop_width, raindrop_height = self.raindrop.rect.size
        # number = random.randrange(100, 150)
        #
        # for i in range(number):
        x = random.randrange(self.screen_width -
                             raindrop_width)
        y = (0 - raindrop_height)

        self.create_raindrop(x, y)

    def create_raindrop(self, x, y):
        """Create a raindrop."""
        raindrop = Raindrop(self)
        raindrop.x = x
        raindrop.rect.x = raindrop.x
        raindrop.y = y
        raindrop.rect.y = raindrop.y

        self.rain_fall.add(raindrop)

    def check_bottom_remove_add_new(self):
        """Checking position of raindrop and remove."""

        for raindrop in self.rain_fall.sprites():
            if raindrop.rect.bottom == self.screen_rect.bottom:
                self.new_raindrop()

            if raindrop.rect.top >= self.screen_rect.bottom:
                self.rain_fall.remove(raindrop)
                print("Hit!!")

                return True

    def update_position(self):
        """Check if the rain is at the bottom,
        then update position of the rain."""
        self.rain_fall.update()
        self.check_bottom_remove_add_new()

    def check_key_event(self):
        """key event to stop screen."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.rain_fall.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    r = FallingRain()
    r.run_program()
