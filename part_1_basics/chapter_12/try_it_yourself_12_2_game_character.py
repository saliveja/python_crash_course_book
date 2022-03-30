import pygame
from try_it_yourself_12_1_blue_sky import MakeScreen


class DrawCharacter:
    """Drawing character and positioning at the center of the screen."""

    def __init__(self, mk_screen):
        """Initializing character and position."""
        self.mk_screen = mk_screen
        self.screen = mk_screen.screen
        self.screen_rect = mk_screen.screen.get_rect()
        self.image = pygame.image.load('Mario.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.make = MakeScreen(self)

    def position(self):
        """Placing the character at the center."""

        self.screen.blit(self.image, self.rect)
