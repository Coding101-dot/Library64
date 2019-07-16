import pygame
from set import Settings
from ship import Ship
import game_functions as gf


# ###############################################################################
# #The main file, alien_Takeover.py, creates a number of important objects used #
# #throughout the game: the settings are stored in ai_settings, the main display#
# #surface is stored in screen, and a ship instance is created in this file as  #
# #well. Also stored in alien_Takeover.py is the main loop of the game, which is#
# #a while loop that calls check_events(), ship.update(), and update_screen().  #
# #alien_Takeover.py is the only file you need to run when you want to play     #
# #Alien Takeover. The other files—settings.py, game_functions.py, ship.py—    #
# #contain code that is imported, directly or indirectly, into this file.       #
# ################################################################################


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Takeover 1")

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update()

        pygame.display.flip()


run_game()
