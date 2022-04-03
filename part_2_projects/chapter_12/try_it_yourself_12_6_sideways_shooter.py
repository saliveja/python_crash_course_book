import pygame
from rocket import Rocket
from settings import Settings


class EmptyScreen:

    def __init__(self, ):
        """Initializing empty screen."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.screen_width = self.screen.get_rect().width
        # self.screen_height = self.screen.get_rect().height
        self.rocket = Rocket(self)

    def run_program(self):
        """running the program."""
        while True:

    def check_events(self):
        """Key events."""
        for event in pygame.event.get():
            self.screen.fill(self.settings.bg_color)
            pygame.display.set_caption("Empty screen")
            if event.type == pygame.KEYDOWN:
                self.key_down(event)
            elif event.type == pygame.KEYUP:
                self.key_up(event)

            pygame.display.flip()


    def key_down(self, event):
        """Key down events."""

        if event.key == pygame.K_q:
            quit()

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True

        elif event.key == pygame.SPACE:
            self.fire_bullet()

    def key_up(self, event):
        """Key up events."""
        if event.key == pygame.SPACE:
            return False

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

    def fire_bullet(self):
        """Create a new bullet and add to the bullet group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        """Update screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.draw()


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
