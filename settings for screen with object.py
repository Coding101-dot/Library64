

# ##########################################################################
# #The settings.py file contains the Settings class. This class only has an#
# #__init__() method, which initializes attributes controlling the game’s ##
# #appearance and the ship’s speed.                                       ##
# ##########################################################################


class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.background_color = (95, 0, 200)
        self.ship_speed_factor = 1.5
