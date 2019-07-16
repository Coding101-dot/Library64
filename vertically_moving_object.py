import pygame

# #############################################################################
# #The ship.py file contains the Ship class. Ship has an __init__() method, an#
# #update() method to manage the ship’s position, and a blitme() method       #
# #to draw the ship to the screen. The actual image of the ship is stored in  #
# #ship.bmp, which is in the images folder.                                   #
###############################################################################

class object:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

#      move left and right without leaving edge of screen
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


#        #update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
