import sys
# tools for exiting the game
from time import sleep
# the sleep function is from python standard library
import pygame
# used for the functionality of the game
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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
        self.stats = GameStats(self)
        # creating an instance that stores statistics
        # the position of the code is important
        # it should be after window is created but before
        # defining other elements
        self.sb = Scoreboard(self)
        # scoreboard instance
        self.ship = Ship(self)
        # making an instance of the ship
        # self refers to the current instance of AlienInvasion
        self.alien = Alien(self)
        # alien instance
        self.bullets = pygame.sprite.Group()
        # making a group of bullets
        self.aliens = pygame.sprite.Group()
        # making a group of aliens
        self._create_fleet()
        # create fleet instance
        self.play_button = Button(self, "Play")
        # making an instance of Button

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            # calling the method _check_events()
            # this is called even if game is inactive
            # to update screen and if player presses q

            if self.stats.game_active:
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # this gives the position of the mouse click
                # so instead of random click resulting in new game
                # it's specifically on the play button
                self._check_play_button(mouse_pos)
                # this checks the play button in relation to the position
                # of the mouse click

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

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens, True, True)
        # this compares the position of all bullets and all aliens and
        # identifies overlap
        # the True arguments tell pygame to delete the bullets and aliens
        # that have collided

        if collisions:
            for aliens in collisions.values():
                # making a for loop with all aliens that have been hit
                self.stats.score += self.settings.alien_points * len(aliens)
                # when bullet hits alien
                # pygame check if there is a dictionary
                # if yes, the value multiplied by the number of aliens in
                # the dictionary will be added to the score
            self.sb.prep_score()
            # new image to update scores
            self.sb.check_high_score()
            # check if there is a new high score
            # if yes, update

        if not self.aliens:
            self.bullets.empty()
            # get rid of remaining bullets
            self._create_fleet()
            # we check if there are any aliens left and if there is not
            # we get rid of any existing bullets and re-create the alien fleet
            # every time all aliens have been shot down a new fleet appears
            self.settings.increase_speed()
            # increasing speed of attributes defined
            self.stats.level += 1
            # if the fleet is destroyed then we level up
            self.sb.prep_level()
            # calling the method prep_level() in scoreboard

    def _fire_bullet(self):
        """Create a new bullet and add it in to the bullets group."""
        # if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        # defining variable new_bullet as class Bullet with access to main
        self.bullets.add(new_bullet)
        # adding the class to the list self.bullets
        # add() is specifically used for pygame

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        # filling the screen with background color
        # takes only one argument
        self.ship.blitme()
        # drawing ship on screen
        self.alien.blitme()
        # drawing alien on screen

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # calling draw_bullet method in Bullet class

        self.aliens.draw(self.screen)
        # drawing each alien in the group to the screen
        # the draw method requires one argument,
        # a surface on which to draw the elements from the group

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
            # if the game is inactive the button will be active
            # to have the button in top layer we include the code at the end

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
        """Check if the fleet is at an edge, the update the position
        of all aliens in the fleet."""
        self._check_fleet_edges()
        # checking if any alien is close to an edge
        self.aliens.update()
        # using update method on aliens group

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # collideany takes two arguments: a sprite and a group
            # looks for any member of the group that has
            # collided with the sprite
            self._ship_hit()
            self._check_aliens_bottom()

            # print("Ship hit!!!")

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # checking if any aliens reached the bottom of the screen
                # this is true when the value is bigger than or equal to the
                # value of the screen
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Respond appropriately if any alien have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                # making a for loop to check if each alien is close to an edge
                # if this returns True, then the whole fleet changes direction

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            # this drops the speed of each alien
        self.settings.fleet_direction *= -1
        # changing direction by multiplying current va lue with -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ship_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()
            # getting rid of remaining aliens and bullets

            self._create_fleet()
            self.ship.center_ship()
            # create new fleet, center ship

            sleep(0.5)
            # making a pause
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            # if the game is inactive the mouse cursor will appear again

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # the game will only start if Play is clicked and the game
        # is not active
        if button_clicked and not self.stats.game_active:
            # checking if mouse click overlaps with the play buttons rect
            self.settings.initialize_dynamic_settings()
            # increasing speed of defined attributes
            # everytime the screen has been cleared of aliens,
            # the speed of the new fleet will increase
            self.stats.reset_stats()
            # resetting game statistics
            self.stats.game_active = True
            # then we set the game_active to True
            self.sb.prep_score()
            # we call this after resetting game statistics
            # this zeroes to scoreboard
            self.sb.prep_level()
            self.sb.prep_ships()
            # showing player how many ships they have
            self.aliens.empty()
            # getting rid of remaining aliens
            self.bullets.empty()
            # getting rid of remaining bullets
            self._create_fleet()
            # creating a new fleet
            self.ship.center_ship()
            # centering the ship
            pygame.mouse.set_visible(False)
            # hiding the mouse cursor during the game


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
