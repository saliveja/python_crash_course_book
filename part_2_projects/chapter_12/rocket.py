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
        self.rect.midleft = self.screen_rect.midleft
        # self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # x and y are defined in pygame
        # self.moving_right = False
        # self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.space = False

    def update(self):
        """update on rockets position."""
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.x += self.settings.rocket_speed
        #
        # if self.moving_left and self.rect.left > 0:
        #     self.x -= self.settings.rocket_speed

        # if self.moving_up and self.rect.top > 0:
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.y = self.y
        # self.rect.x = self.x

    def draw(self):
        """Draw the rocket on the screen."""
        self.screen.blit(self.image, self.rect)
