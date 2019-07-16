import sys
import pygame
##################################################################################
# #The game_functions.py file contains a number of functions that carry out      #
# #the bulk of the work in the game. The check_events() function detects relevant#
# #events, such as keypresses and releases, and processes each of these          #
# #types of events through the helper functions check_keydown_events() and       #
# #A Ship That Fires Bullets 257                                                 #
# #check_keyup_events(). For now, these functions manage the movement of         #
# #the ship. The game_functions module also contains update_screen(), which      #
# #redraws the screen on each pass through the main loop.                        #
#  ###############################################################################
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.background_color)
    ship.blitme()
