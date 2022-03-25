import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        # loading image of alien
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        # placing alien in upper left corner
        # adding space to the left
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)
