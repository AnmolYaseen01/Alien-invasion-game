# game.py
import pygame
from pygame.sprite import Group
from settings import WIDTH, HEIGHT, WHITE, GREEN, RED
from ship import Ship
from bullet import Bullet
from alien import Alien
from utils import check_events, update_screen, display_text, draw_button

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship()
    bullets = Group()
    aliens = Group()
    alien_spawn_timer = Alien.spawn_delay

    clock = pygame.time.Clock()

    running = False
    score = 0

    while True:
        if not running:
            screen.fill((0, 0, 0))
            display_text(screen, "Alien Invasion", 72, WIDTH // 2, HEIGHT // 4)
            draw_button(screen, pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 50), GREEN, "Start", WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 50).collidepoint(event.pos):
                        running = True
                        # Reset the game state
                        ship = Ship()
                        bullets = Group()
                        aliens = Group()
                        score = 0

            pygame.display.flip()
            clock.tick(60)
            continue

        check_events(ship, bullets)
        ship.update()

        alien_spawn_timer -= 1
        if alien_spawn_timer <= 0:
            alien = Alien()
            aliens.add(alien)
            alien_spawn_timer = Alien.spawn_delay

        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

        if collisions:
            for aliens_hit in collisions.values():
                score += len(aliens_hit)

        if pygame.sprite.spritecollideany(ship, aliens):
            running = False

        update_screen(screen, ship, bullets, aliens, score)

        clock.tick(60)

if __name__ == "__main__":
    main()
    