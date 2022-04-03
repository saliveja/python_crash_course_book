import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to manage the ship."""

    def __init__(self, stars_main):
        """Initialize the ship and set its starting position."""

        super().__init__()
        # Ship inherits from Sprite

        self.screen = stars_main.screen
        self.screen_rect = stars_main.screen.get_rect()
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft
        self.x = float(self.rect.x)

    def update(self):
        """Drawing and updating the stars on the screen."""
        self.screen.blit(self.image, self.rect)
