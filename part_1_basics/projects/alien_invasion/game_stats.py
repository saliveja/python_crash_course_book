class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        # we reset stats every time a new game starts
        # ship_limit refers to the number of ships the player have access
        # to in the game. It is defined in Settings
        self.score = 0
        # we reset the score every time a new game starts
