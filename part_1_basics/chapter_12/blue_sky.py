import pygame
import sys
# from try_it_yourself_12_2_game_character import DrawCharacter
from rocket import Rocket
from settings import Settings


class BlueSky:
    """Main program for the game Blue Sky."""

    def __init__(self):
        """Initializing blue screen"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # making a variable self.screen which creates the window with
        # the specified values
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Spaceship")
        # on top of the window this message is printed
        self.rocket = Rocket(self)
        # making variable calling the class DrawCharacter
        # 'self' gives access to the programs resources ie. screen
        # 'self' is referring to __init_(self) to get access to
        # all the self.variables

    def run_game(self):
        """Main loop of the game."""
        while True:
            self.events()
            self.rocket.update()
            self.display_screen()

    def events(self):
        """Checking key events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_down(event)

            elif event.type == pygame.KEYUP:
                self.key_up(event)

    def key_up(self, event):
        """Key up events."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def key_down(self, event):
        """ Key down events"""
        if event.type == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    def display_screen(self):
        """Displaying screen."""
        self.screen.fill(self.settings.bg_color)
        # filling screen with background color
        self.rocket.draw()
        # drawing picture on the screen
        pygame.display.flip()
        # updating surface area


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
