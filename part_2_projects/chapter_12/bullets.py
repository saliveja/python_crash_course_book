import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, blue_sky):
        """Create a bullet object at the ships current position."""
        super().__init__()
        self.screen = blue_sky.screen
        self.settings = blue_sky.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        self.rect.midright = blue_sky.rocket.rect.midright
        # this defined where bullets in rocket starts
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        self.x += self.settings.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
