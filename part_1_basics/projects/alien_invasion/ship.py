import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        # the screen equals the screen in AlienInvasion
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # placing the ship in its current location
        self.image = pygame.image.load('images/ship.bmp')
        # loading the image
        self.rect = self.image.get_rect()
        # accessing the ships surface rect attribute
        # to be able to position later
        self.rect.midbottom = self.screen_rect.midbottom
        # ships position specified to bottom center
        self.x = float(self.rect.x)
        # using float to store decimal values for ship in horizontal position
        # rect attribute x only stores integers
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.right return the x-coordinates of the right edge
            # if the value is less tha self.screen_rect.right
            # the ships hasn't reached the edge yet
            self.rect.x += self.settings.ship_speed
            # the speed is now assigned to a variable in settings module
            # whenever we want to change the speed we only need
            # to change it there

        if self.moving_left and self.rect.left > 0:
            # if the value of self.rect is more than 0
            # hte ship hasn't reached the edge
            # remember that 0,0 starts in the upper left corner
            self.rect.x -= self.settings.ship_speed

        self.rect.x = self.x
        # the speed variable for moving right or left is connected
        # to decimal values for ships horizontal position

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # position (0, 0) means the upper left corner
