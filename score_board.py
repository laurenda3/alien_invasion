import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (0, 0, 128)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = f"Score: {self.stats.score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = f"High Score: {self.stats.high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
