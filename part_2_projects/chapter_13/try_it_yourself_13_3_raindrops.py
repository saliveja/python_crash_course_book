import pygame
import random as random


class Rain:

    def __init__(self):
        """Initializing the program."""
        pygame.init()
        self.bg_color = (100, 30, 200)
        self.screen_width = 4000
        self.screen_height = 1600
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Rain")
        self.rain = Rain(self)
        self.rain_fall = pygame.sprite.Group()
        self.create_raindrops()

    def create_raindrops(self):
        """Drawing a grid of stars on the screen."""
        number = random.randrange(555, 1333)
        # making variable for the wished randomness of numbers

        for i in range(number):
            # for integer within the range defined in number
            x = random.randrange(
                self.screen_width - self.star.star_width)
            # Randomizing stars horizontally
            y = random.randrange(
                self.screen_height - self.star.star_height)
            # randomizing stars vertically
            self.create_raindrop(x, y)
            # calling for the method create_star with the randomization
            # defined above

    def create_raindrop(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        # creating a space at the top of the screen which is the height
        # of one alien
        self.aliens.add(alien)



