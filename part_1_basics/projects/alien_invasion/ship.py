import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # placing the ship in its current location
        self.image = pygame.image.load('images/ship.bmp')
        # loading the image
        self.rect = self.image.get_rect()
        # accessing the ships surface rect attribute
        # to be able to position later
        self.rect.midbottom = self.screen_rect.midbottom
        # ships position specified to bottom center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # position (0, 0) means the upper left corner
