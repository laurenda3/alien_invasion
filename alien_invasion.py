import sys
import pygame
from button import Button
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from score_board import Scoreboard



def run_game():
    # Initialize pygame and settings
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")


    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats) 

    # Create a ship
    ship = Ship(ai_settings, screen)

    # Create a group to store bullets
    bullets = pygame.sprite.Group()

    # Create a group to store aliens
    aliens = pygame.sprite.Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main game loop
def run_game():
    # Initialize pygame and settings
    pygame.init()
    ai_settings = Settings()
    screen = screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ai_settings.screen_width = screen.get_rect().width
    ai_settings.screen_height = screen.get_rect().height

    pygame.display.set_caption("Alien Invasion")

    # Create Play button
    play_button = Button(ai_settings, screen, "Play")

    # Game stats and scoreboard
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats)

    # Player's ship
    ship = Ship(ai_settings, screen)

    # Bullets and aliens
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main game loop
    while True:
        gf.check_events(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, stats, score_board)
            gf.update_aliens(ai_settings, stats, screen, score_board, ship, aliens, bullets)

        # Check for victory
        if not aliens:
            display_victory_message(screen, ai_settings)
            stats.game_active = False # Stop the game after victory

        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens, bullets, play_button)



def display_victory_message(screen, ai_settings):
    """Display the 'You Won!' message after all aliens are defeated."""
    font = pygame.font.SysFont(None, 80)
    text = font.render("WINNER WINNER CHICKEN DINNER!!", True, (0, 255, 0))  # Green color
    text_rect = text.get_rect()
    text_rect.center = screen.get_rect().center  # Center the text

    screen.blit(text, text_rect)
    pygame.display.flip()

    # Wait for a key press to restart the level or move to the next level
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press ENTER to proceed
                    waiting = False









run_game()

