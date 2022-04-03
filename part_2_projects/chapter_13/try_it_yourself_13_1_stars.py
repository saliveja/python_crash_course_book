import sys
import pygame
from stars import Star


class EmptyScreen:

    def __init__(self, ):
        """Initializing empty screen."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Stars")
        self.star = Star(self)

    def run_program(self):
        """running the program."""
        while True:
            self.update_screen()

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.star.update()
        pygame.display.flip()


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
