import pygame


class EmptyScreen:

    def __init__(self, ):
        """Initializing empty screen."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 2000
        self.screen_height = 800
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.image = pygame.image.load('spaceship.bmp')
        self.rect = self.image.get_rect()

    def run_program(self):
        """running the program."""
        while True:
            for event in pygame.event.get():
                self.screen.fill(self.bg_color)
                pygame.display.set_caption("Empty screen")
                if event.type == pygame.KEYDOWN:
                    self.key_down(event)
                elif event.type == pygame.KEYUP:
                    self.key_up(event)

            pygame.display.flip()

    def key_down(self, event):
        """Key down events."""
        if event.key == pygame.K_RIGHT:
            self.image = pygame.image.load('spaceship.bmp')
            self.rect = self.image.get_rect()
            self.screen.blit(self.image, self.rect)
            
        elif event.key == pygame.K_LEFT:
            quit()
        elif event.key == pygame.K_DOWN:
            self.screen = pygame.display.set_mode(2000, 800)

        elif event.key == pygame.K_UP:
            self.bg_color = (100, 255, 200)

    def key_up(self, event):
        """Key up events."""
        if event.key == pygame.K_RIGHT:
            return False
        elif event.key == pygame.K_LEFT:
            return False
        elif event.key == pygame.K_DOWN:
            return False
        elif event.key == pygame.K_UP:
            return False


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
