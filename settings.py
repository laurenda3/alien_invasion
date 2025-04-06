class Settings():
    """ A class to store all settings for Alien Invasion. """
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 128, 0
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = -1
        self.fleet_drop_speed = 2
        self.fleet_direction = 1


        # Score settings
        self.alien_points = 10 # Points for killing the alien.
