import pygame
import sys
# from try_it_yourself_12_2_game_character import DrawCharacter
from try_it_yourself_12_4_rocket import DrawCharacter


class MakeScreen:
    """Making a blue screen."""

    def __init__(self):
        """Initializing blue screen"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        # making a variable self.screen which creates the window with
        # the specified values

        pygame.display.set_caption("Spaceship")
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
