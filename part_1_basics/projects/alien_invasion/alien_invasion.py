# tools for exiting the game
import sys
# used for the functionality of the game
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # creating a game window - 'surface'
        # the variable self.screen works in all methods in the class
        # (0, 0) and FULLSCREEN tells python to figure out a size
        # that will fill the screen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        # assigns the name Alien Invasion to the game

        self.ship = Ship(self)
        # making an instance of the ship
        # self refers to the current instance of AlienInvasion

        self.alien = Alien(self)

        self.bullets = pygame.sprite.Group()
        # making a group of bullets
        self.aliens = pygame.sprite.Group()
        # making a group of aliens
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            # calling the method _check_events()
            self.ship.update()
            # refers to the method update in the class Ship
            # if self.moving_right then it will move one pixel to the right
            self.bullets.update()
            # refers to the method update in class Bullets
            self._update_bullets()
            # refers to the help method in AI
            self._update_aliens()
            self._update_screen()
            # calling the method to constantly be updating what is happening
            # on the screen
            # giving the method access to the group aliens

    def _check_events(self):
        """Respond to key presses."""

        for event in pygame.event.get():
            # an event is the action of a user
            # pygame.event.get() returns a list of events
            # that have taken place since last time the loop was called
            if event.type == pygame.KEYDOWN:
                # if a key is pressed down
                self._check_keydown_events(event)
                # going to the helper method which will move the ship
                # bcs statement is True
            elif event.type == pygame.KEYUP:
                # if the key is not pressed anymore
                self._check_keyup_events(event)
                # going to helper method, statement is False

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
        elif event.key == pygame.K_SPACE:
            self.bullets._fire_bullets = False

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            # if the user clicks on the letter Q
            # the user exits the game
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            # and that key is right arrow
            self.ship.moving_right = True
            # moving right is True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            # if the left arrow key is no longer pressed
            # statement is True and the spaceship will move to the left
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            # the spaceship will fire bullets

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            # in pygame we can't modify lists or groups
            # copy enables us to modify bullets inside the loop
            if bullet.rect.bottom <= 0:
                # if the bullet reaches value 0
                # which is at the top os the screen
                self.bullets.remove(bullet)
                # the bullet will be removed

    def _fire_bullet(self):
        """Create a new bullet and add it in to the bullets group."""
        # if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        # defining variable new_bullet as class Bullet with access to main
        self.bullets.add(new_bullet)
        # adding the new bullet to the list
        # add() is specifically used for pygame

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        # filling the screen with background color
        # takes only one argument
        self.ship.blitme()
        self.alien.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # calling draw_bullet method in Bullet class

        self.aliens.draw(self.screen)
        # drawing each alien in the group to the screen
        # the draw method requires one argument,
        # a surface on which to draw the elements from the group

        pygame.display.flip()
        # Makes the most recent screen visible
        # continuously updating

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        # creating an alien
        alien_width, alien_height = alien.rect.size
        # using attribute size with the width and height of a rect object
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # calculating the available space for aliens to see how many we
        # can fit on the screen
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
                # nested loops to create the aliens and the rows

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        # creating a space at the top of the screen which is the height
        # of one alien
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the position of all aliens in the fleet."""
        self.aliens.update()
        # using update method on aliens group


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
