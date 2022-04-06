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
        self.game_active = False
        self.create_rain_grid()

    def run_program(self):
        """running the program."""
        while True:
            self.game_active = True
            self.check_key_event()
            self.update_screen()
            self.rain_fall.update()
            self.check_rain_edges()

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

    def check_rain_edges(self):
        """if raindrop reached the bottom, loop from the beginning."""
        raindrop = Raindrop()
        for raindrop in self.rain_fall.sprites():
            if raindrop.rain_edges():
                self.restart_rain()
                break

    def rain_edges(self):
        """Checking position of raindrops."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def restart_rain(self):
        """Start the rain again from the top."""
        for raindrop in self.rain_fall.sprites():
            raindrop.rect.x = 0
            self.raindrop.direction = 1

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.rain_fall.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    r = FallingRain()
    r.run_program()
