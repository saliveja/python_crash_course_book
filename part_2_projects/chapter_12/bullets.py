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

        self.rect = pygame.Rect((0, 0), self.settings.bullet_width,
                                self.settings.bullet_height)

        self.rect.bottomleft = blue_sky.rocket.rect.bottomleft
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
