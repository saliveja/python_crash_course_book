import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, falling_rain, midbottom=None):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = falling_rain.screen
        # self.settings = ai_game.settings
        # # we defined the speed in Settings
        self.screen_rect = falling_rain.screen.get_rect()
        self.image = pygame.image.load('images/raindrop.bmp')
        # loading image of alien
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        # placing alien in upper left corner
        # adding space to the left
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.width = 3
        self.height = 3
        self.speed = 3
        self.rect.top = self.screen_rect.top

    def draw(self):
        """Draw the raindrop at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right or left."""
        self.y += (self.speed * self.midbottom)
        # speed id defined in init
        # y is referring to vertical axis
        self.rect.y = self.y
