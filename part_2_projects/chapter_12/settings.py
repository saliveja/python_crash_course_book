class Settings:
    """Settings for the game Bly sky."""

    def __init__(self):
        """Initializing settings."""
        self.screen_width = 1000
        # defining width
        self.screen_height = 600
        # defining height
        self.bg_color = (40, 180, 255)
        # setting a blue color
        self.bullet_color = (255, 255, 255)
        self.rocket_speed = 5
        self.rocket_drop_speed = 10
