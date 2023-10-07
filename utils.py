# utils.py
import pygame

def check_events(ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot(bullets)

def update_screen(screen, ship, bullets, aliens, score):
    screen.fill((0, 0, 0))
    ship.update()
    ship.draw(screen)
    bullets.update()
    bullets.draw(screen)
    aliens.update()
    aliens.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

def display_text(screen, text, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect.topleft)

def draw_button(screen, rect, color, text, text_color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect.topleft)
