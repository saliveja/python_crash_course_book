import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # we defined the speed in Settings

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

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        # tracking position of alien
        # alien_speed is defined in Settings
        self.rect.x = self.x
        # using self.x to update the aliens position

    def check_edges(self):
        """Return True is alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        # the alien is at the edge of the right side of the screen if
        # its rect is bigger than or equal to the screens rect
        # the alien is at the left edge if the rect is less than or equal to 0
