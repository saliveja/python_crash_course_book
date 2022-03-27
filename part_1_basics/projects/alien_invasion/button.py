import pygame.font


# importing font module from pygame to be able to render text on screen


class Button:

    def __init__(self, ai_game, msg):
        """Initializing button attributes."""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        # size is in pixels
        self.button_color = (0, 255, 0)
        # color bright green
        self.text_color = (255, 255, 255)
        # color white
        self.font = pygame.font.SysFont(None, 48)
        # setting dimensions and properties of the button
        # None means default font, 48 is the size of the text

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
        # the text for the button

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        # render() turns the text into an image which is stored in
        # self.msg_image
        # if there is no background color pygame will try to render the font
        # with a transparent background
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        # placing the image in the center of the screen

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        # screen.fill draws color and proportion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # draws the image to the screen
