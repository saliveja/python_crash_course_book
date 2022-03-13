import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    # the bullet class inherits from Sprite
    # with Sprite we can group all elements and act on all at the same time

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # creating a variable we can use throughout the class which represents
        # the color of the bullet

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        # the bullets are not based of images so instead we build them from
        # scratch. This requires giving the coordinates from upper left corner

        self.rect.midtop = ai_game.ship.rect.midtop
        # assigning position for bullets
        self.y = float(self.rect.y)
        # making it possible to have decimals for the position of bullets

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        # when a bullet is fired it moved up the screen
        # this mean a constant decrease of y coordinate value
        self.rect.y = self.y
        # we store self.y in variable self.rect.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
