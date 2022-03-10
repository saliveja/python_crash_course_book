import pygame
import sys


class MakeScreen:
    """Making a blue screen."""

    def __init__(self):
        """Initializing blue screen"""
        pygame.init()
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (40, 180, 255)
        # setting a blue color

    def displayScreen(self):
        """Displaying screen."""
        while True:
            self.screen = pygame.display.set_mode((self.screen_width,
                                                   self.screen_height))

            pygame.display.set_caption("Blue screen")

            self.screen.fill(self.bg_color)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    mk = MakeScreen()
    mk.displayScreen()
