import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()