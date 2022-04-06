import pygame
import sys
# from try_it_yourself_12_2_game_character import DrawCharacter
from try_it_yourself_12_4_rocket import DrawCharacter
from settingstry import SettingsTry


class MakeScreen:
    """Making a blue screen."""

    def __init__(self):
        """Initializing blue screen"""
        pygame.init()
        self.settings = SettingsTry()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # making a variable self.screen which creates the window with
        # the specified values

        pygame.display.set_caption("Spaceship")
        # on top of the window this message is printed
        self.draw = DrawCharacter(self)
        # making variable calling the class DrawCharacter
        # 'self' gives access to the programs resources ie. screen
        # 'self' is referring to __init_(self) to get access to
        # all the self.variables

    def runGame(self):
        while True:
            self.displayScreen()
            self.events()

    def displayScreen(self):
        """Displaying screen."""
        while True:
            self.screen.fill(self.settings.bg_color)
            # filling screen with background color

            self.draw.position()
            # drawing picture on the screen

            pygame.display.flip()

    def events(self):
        """Ckecking key events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyDownEvents()

            elif event.type == pygame.KEYUP:
                self.keyUpEvents()

    def keyUpEvents(self, event):
        """Key up events."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.moving_left = False

        elif event.key == pygame.K_UP:
            self.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def keyDownEvents(self, event):
        """ Key down events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.key == pygame.K_RIGHT:
            self.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.moving_left = True

        elif event.key == pygame.K_UP:
            self.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.moving_down = True


if __name__ == '__main__':
    mk = MakeScreen()
    mk.runGame()
