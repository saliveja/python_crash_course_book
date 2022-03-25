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

  def _update_screen(ai_settings, screen, ship, aliens, bullets):
        """Update images on the screen, and flip to the new screen."""

        screen.fill(ai_settings.bg_color)
        # filling the screen with background color
        # takes only one argument

        for bullet in bullets.sprites():
            bullet.draw_bullet()
            # calling draw_bullet method in Bullet class
        ship.blitme()
        # drawing the ship on the screen
        aliens. draw(screen)
        # drawing each alien in the group to the screen

        pygame.display.flip()
        # Makes the most recent screen visible
        # continuously updating

  def create_fleet(self):
      """Create a full fleet of aliens."""

      alien = Alien(self)
      # creating an alien
      aliens.add(alien)

      alien_width = alien.rect.width
      # store the alien width in a new variable
      available_space_x = ai_settings.screen.width - 2 * alien_width
      # calculating the available space for aliens to see how many we
      # can fit on the screen
      number_aliens_x = int(available_space_x / (2 * alien_width))


      for alien_number in range(number_alien_x):
          alien = Alien(ai_settings, screen)
          alien.x = alien_width + 2 * alien_width * alien_number
          alien.rect.x = alien.x
          self.aliens.add(alien)
