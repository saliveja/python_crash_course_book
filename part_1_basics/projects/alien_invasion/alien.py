import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init(self, ai_settings, screen):
        """Initialize the alien and set it's starting position."""

        super(Alien, self)._init_()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(image.bmp)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at it's current location."""

        self.screen.blit(self.image, self.rect)
