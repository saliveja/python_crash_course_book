import pygame.font


class Scoreboard:
    """A class to report scoring information>"""

    def __init__(self, ai_game):
        """Initializing scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        # round() rounds a decimal number to a set number of decimals
        # this is defined with the second argument
        # if the scond arument is negative round() wil round the value to
        # the nearest 10, 100 and so on, stored in variable rounded_score
        score_str = "{:,}".format(rounded_score)
        # using comma separators ie. 1,000,000 instead if 1000000
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
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # drawing high score in top right corner
        self.screen.blit(self.level_image, self.level_rect)
        # draws the level on the screen

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        # using round() to  round numbers to the closest 10, 100, 1000 etc
        # using comma as separation in lrge numbers
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        # generating an image of the high score

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = self.score_rect.top
        # top attribute is the same  as image rect

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            # checking current score against high score
            # if the current score is higher than the high score, the new
            # high score will be displayed
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.settings.bg_color)
        # creates an image from values stored in stats.level

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        # sets the image right attribute to that of the scores right attribute
        self.level_rect.top = self.score_rect.bottom + 10
        # the level is places 10 pixels below the score
