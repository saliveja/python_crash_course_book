import pygame.font


class Scoreboard:
    """A class to report scoring information>"""

    def __init__(self):
        """Initializing scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        # turning the stats value into a string
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        # using render turns the score info into an image
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        # placing image in upper right corner, 20 pixels from the screens edge
        self.score_rect.top = 20
        # and 20 pixels from the top

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        # draws the score image  on the screen where rect specified
