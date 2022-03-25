class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initializing the games setting."""

        self.screen_width = 1200
        # screen width is 1200 pixels
        self.screen_height = 800
        # screen height is 800 pixels
        self.bg_color = (230, 230, 230)
        # the color of the background is light grey
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.bullet_width = 3
        # the width of the bullet is 3 pixels
        self.bullet_height = 15
        # the height of the bullet is 15 pixels
        self.bullet_color = (60, 60, 60)
        # the color of the bullet is dark grey
        self.bullets_allowed = 3
        self.alien_speed = 1.0
