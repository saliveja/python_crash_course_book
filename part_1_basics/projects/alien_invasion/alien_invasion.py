# tools for exiting the game
import sys
# used for the functionality of the game
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()
        # initialized background setting
        self.settings = Settings()
        # making an instance of class Settings
        # with this imported class we can change the color and
        # the screen by changing it in this class instead of
        # changing it through the program which is inefficient

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # creating a game window - 'surface'. Numbers are pixels
        # creating a variable that works in all methods in the class
        pygame.display.set_caption("Alien Invasion")
        # assigns the name Alien Invasion to the game

        self.ship = Ship(self)
        # making an instance of the ship
        # self refers to the current instance of AlienInvasion

        self.bg_color = (230, 230, 230)
        # setting the background color
        # colors in Pygame are RGB colors

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            # calling the method _check_events()
            self.ship.update()
            # refers to the method update in the class Ship
            # if self.moving_right then it will move one pixel to the right
            self._update_screen()
            # calling the method to constantly be updating what is happening
            # on the screen

    def _check_events(self):
        """Respond to key presses and mouse events."""

        for event in pygame.event.get():
            # an event is the action of a user
            # pygame.event.get() returns a list of events
            # that have taken place since last time the loop was called
            if event.type == pygame.QUIT:
                # if the user clicks on the game windows close button
                # the user exits the game
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # if a key is pressed down
                self._check_keydown_events(event)
                # going to the helper method which will move the ship
                # bcs statement is True
            elif event.type == pygame.KEYUP:
                # if the key is not pressed anymore
                self._check_keyup_events(event)
                # going to helper method which will

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # if that key is arrow right
            self.ship.moving_right = True
            # we move ship one pixel to the right every time the
            # right arrow key is pressed
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            # if the left arrow key is pressed moving_left is true
        elif event.key == pygame.K_q:
            sys.exit()
            # pressing 'q' ends the game

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # and that key is right arrow
            self.ship.moving_right = False
            # moving right is False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            # if the left arrow key is no longer pressed
            # statement is False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        # filling the screen with background color
        # takes only one argument

        self.ship.blitme()
        # drawing the ship on the screen

        pygame.display.flip()
        # Makes the most recent screen visible
        # continuously updating


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
