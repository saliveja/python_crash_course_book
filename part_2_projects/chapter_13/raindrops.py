import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, falling_rain):
        """Initializing."""
        super().__init__()

        self.screen = falling_rain.screen
        self.screen_rect = falling_rain.screen.get_rect()
        self.image = pygame.image.load('images/raindrop_black.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rain_speed = 2
        self.raindrop_height = 10
        self.raindrop_width = 10
        self.direction = 1
        self.y = float(self.rect.y)

    def update(self):
        """Rain falling."""
        self.y += (self.rain_speed * self.direction)
        self.rect.y = self.y
