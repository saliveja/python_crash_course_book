import sys
import pygame
import random as random
from raindrops import Rain


class FallingRain:

    def __init__(self):
        """Initializing the program."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 4000
        self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Falling rain")
        self.rain = Rain(self)
        self.rain_fall = pygame.sprite.Group()
        self.create_rain_grid()

    def run_program(self):
        """running the program."""
        while True:
            self.update_screen()

    def create_rain_grid(self):
        """Drawing a grid of raindrops on the screen."""
        number = random.randrange(555, 1333)

        for i in range(number):
            x = random.randrange(
                self.screen_width - self.rain.rain_width)
            y = random.randrange(
                self.screen_height - self.rain.rain_height)
            self.create_raindrop(x, y)

    def create_raindrop(self, x, y):
        """Create a raindrop."""
        raindrop = Rain(self)
        raindrop.rect.x = x
        raindrop.rect.y = y
        self.rain_fall.add(raindrop)

    def stop_screen(self):
        """key event to stop screen."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.rain_fall.update()
        self.stop_screen()
        pygame.display.flip()


if __name__ == '__main__':
    r = FallingRain()
    r.run_program()
