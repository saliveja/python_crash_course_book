import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, falling_rain):
        """Initializing."""
        super().__init__()

        self.screen = falling_rain.screen
        self.screen_rect = falling_rain.screen.get_rect()
        self.image = pygame.image.load('images/raindrop_black.bmp')
        self.rect = self.image.get_rect()
        self.rain_width = 50
        self.rain_height = 50
        self.rect.topleft = self.screen_rect.topleft
        self.x = self.rect.x

    def update(self):
        """Draw the raindrop at its current location."""
        self.screen.blit(self.image, self.rect)
