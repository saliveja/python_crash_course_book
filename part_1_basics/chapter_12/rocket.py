import pygame
from settings import Settings


class Rocket:
    """A class for the rocket."""

    def __init__(self, blue_sky):
        """Initializing rocket."""
        self.screen = blue_sky.screen
        self.settings = Settings()
        self.screen_rect = blue_sky.screen.get_rect()
        self.image = pygame.image.load('spaceship.bmp')
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)

    def update(self):
        """update on rockets position."""
        if self.moving_right and self.rect.right < self.screen.rect.right:
            self.x += self.settings.rocket_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        if self.moving_up and self.rect.up > 0:
            self.x -= self.settings.rocket_speed

        if self.moving_down and self.rect.down < self.screen.rect.down:
            self.x += self.settings.rocket_speed

    def draw(self):
        """Draw the rocket on the screen."""
        self.screen.blit(self.image, self.rect)
