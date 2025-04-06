
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        # Align the bullet to the ship's center horizontally and just above it
        self.rect.centerx = ship.rect.centerx - 15 # Align with the center of the ship
        self.rect.top = ship.rect.top - ai_settings.bullet_height   # Just above the ship's top

        # Store the bullet's position as a decimal value for more precise movement
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # Debugging: Check where the bullet is being created
        #print(f"Bullet spawned at: x={self.rect.centerx}, y={self.rect.top}")

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
