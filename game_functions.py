import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_play_button(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset game stats.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard.
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        score_board.prep_ships()

        # Clear aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create new fleet and center the ship.
        gf.create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, score_board, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # Draw the score
    score_board.show_score()

    # Draw the play button if te game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(bullets, aliens, ai_settings, stats, score_board):
    """Update position of bullets, get rid of old bullets, and check for bullet collisions with aliens."""
    # Update bullet positions.
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in bullets.copy():
        collisions = pygame.sprite.spritecollide(bullet, aliens, True)
        if collisions:
            bullets.remove(bullet)
            stats.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_of_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    return int(available_space_y / (2 * alien_height))

def update_aliens(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """Check if the fleet is at an edge, and update the positions of all aliens."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, score_board, ship, aliens, bullets)


def ship_hit(ai_settings, screen, stats, score_board, ship, aliens, bullets):
    """Respond to the ship being hit by an alien."""
    stats.game_active = False
    show_game_over(screen)


def show_game_over(screen):
    """Display 'Game Over' message on screen."""
    font = pygame.font.SysFont(None, 96)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = screen.get_rect().center
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Pause so player can see the message
    pygame.time.wait(3000)



def check_fleet_edges(ai_settings, aliens):
    """Respond if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the fleet and change its direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_play_button(ai_settings, screen, stats, score_board, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset game settings
        stats.reset_stats()
        stats.game_active = True

        # Empty aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset score
        score_board.prep_score()
