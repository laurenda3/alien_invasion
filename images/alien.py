import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and sets its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_ret()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect = self.rect.height

        # Store te alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
