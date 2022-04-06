import sys
import pygame
from pygame.sprite import Sprite
import random as random
from raindrops import Raindrop


class FallingRain:

    def __init__(self):
        """Initializing the program."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 4000
        self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Falling rain")
        self.raindrop = Raindrop(self)
        self.rain_fall = pygame.sprite.Group()
        self.create_rain_grid()

    def run_program(self):
        """running the program."""
        while True:
            # self.raindrop.movement()

            self.check_key_event()

            self.update_screen()
            self.rain_fall.update()

    def create_rain_grid(self):
        """Drawing a grid of raindrops on the screen."""
        number = random.randrange(500, 1000)

        raindrop_width, raindrop_height = self.raindrop.rect.size

        for i in range(number):
            x = random.randrange(
                self.screen_width - raindrop_width)
            y = random.randrange(
                self.screen_height - raindrop_height) - self.screen_height

            self.create_raindrop(x, y)

    def create_raindrop(self, x, y):
        """Create a raindrop."""
        raindrop = Raindrop(self)
        raindrop.x = x
        raindrop.rect.x = raindrop.x
        raindrop.y = y
        raindrop.rect.y = raindrop.y

        self.rain_fall.add(raindrop)

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
