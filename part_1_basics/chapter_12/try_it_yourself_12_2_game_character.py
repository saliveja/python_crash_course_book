import pygame


class DrawCharacter:
    """Drawing character and positioning at the center of the screen."""

    def __init__(self, mk_screen):
        """Initializing character and position."""

        self.screen = mk_screen.screen
        self.screen_rect = mk_screen.screen.get_rect()
        self.image = pygame.image.load('Mario.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def position(self):
        """Placing the character at the center."""

        self.screen.blit(self.image, self.rect)
