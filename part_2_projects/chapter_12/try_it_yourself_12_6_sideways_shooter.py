import sys
import pygame
from settings import Settings
from rocket import Rocket
from bullets import Bullet


class EmptyScreen:

    def __init__(self):
        """Initializing empty screen."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways shooter")
        self.screen_rect = self.screen.get_rect()
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def run_program(self):
        """running the program."""
        while True:
            self.check_events()
            self.rocket.update()
            self.bullets.update()
            self.update_bullet()
            self.update_screen()

    def check_events(self):
        """Key events."""
        for event in pygame.event.get():
            self.screen.fill(self.settings.bg_color)
            if event.type == pygame.KEYDOWN:
                self.key_down(event)
            elif event.type == pygame.KEYUP:
                self.key_up(event)

    def key_down(self, event):
        """Key down events."""

        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def key_up(self, event):
        """Key up events."""
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

        elif event.key == pygame.K_SPACE:
            return False

    def update_bullet(self):
        """Update position of bullets, removing old ones."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right == self.screen_rect.right:
                self.bullets.remove(bullet)

    def fire_bullet(self):
        """Create a new bullet and add to the bullet group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        """Update screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.draw()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
