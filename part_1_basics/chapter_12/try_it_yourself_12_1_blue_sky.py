import pygame
import sys
from try_it_yourself_12_2_game_character import DrawCharacter


class MakeScreen:
    """Making a blue screen."""

    def __init__(self):
        """Initializing blue screen"""
        pygame.init()

        self.screen_width = 600
        # defining width
        self.screen_height = 500
        # defining height
        self.bg_color = (40, 180, 255)
        # setting a blue color

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        # making a variable self.screen which creates the window with
        # the specified values

        pygame.display.set_caption("Mario")
        # on top of the window this message is printed
        self.draw = DrawCharacter(self)
        # making variable calling the class DrawCharacter
        # 'self' gives access to the programs resources ie. screen
        # 'self' is referring to __init_(self) to get access to
        # all the self.variables

    def displayScreen(self):
        """Displaying screen."""
        while True:
            self.screen.fill(self.bg_color)
            # filling screen with background color

            self.draw.position()
            # drawing mario on the screen

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    mk = MakeScreen()
    mk.displayScreen()
