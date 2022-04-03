import sys
import pygame
from stars import Star


class EmptyScreen:

    def __init__(self, ):
        """Initializing empty screen."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 4000
        self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Stars")
        self.star = Star(self)
        self.stars = pygame.sprite.Group()
        self.create_star_grid()

    def run_program(self):
        """running the program."""
        while True:
            self.star.update()
            self.update_screen()

    def create_star_grid(self):
        """Drawing a grid of stars on the screen."""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_star_x = available_space_x // (2 * star_width)
        star_height = self.star.rect.height

        available_space_y = (self.screen_height -
                             (3 * star_height) - star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self.create_star(star_number, row_number)

    def create_star(self, star_number, row_number):
        """Create star and place in the grid."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def update_screen(self):
        """Updating screen."""
        self.screen.fill(self.bg_color)
        self.star.update()
        self.create_star_grid()
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    es = EmptyScreen()
    es.run_program()
