def _check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # if that key is arrow right
        self.ship.moving_right = True
        # we move ship one pixel to the right every time the
        # right arrow key is pressed
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
        # if the left arrow key is pressed moving_left is true
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()
        # if the space bar is pressed down, the ship will fire bullets
    elif event.key == pygame.K_q:
        sys.exit()
        # pressing 'q' ends the game
