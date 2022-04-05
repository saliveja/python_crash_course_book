import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to create the star."""

    def __init__(self, stars_main):
        """Initializing."""

        super().__init__()

        self.screen = stars_main.screen
        self.screen_rect = stars_main.screen.get_rect()
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.star_width = 100
        self.star_height = 100
        self.rect.topleft = self.screen_rect.topleft
        # self.x = float(self.rect.x)
        self.x = self.rect.x

    def update(self):
        """Drawing and updating the stars on the screen."""
        self.screen.blit(self.image, self.rect)
