import pygame


class EmptyScreen:

    def __init__(self, ):
        """Initializing empty screen."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Stars")

        self.rect = self.image.get_rect()

    def run_program(self):
        """running the program."""
        while True:
            pygame.display.flip()


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
