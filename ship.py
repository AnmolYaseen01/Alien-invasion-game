# ship.py
import pygame
from settings import WIDTH, SHIP_SPEED
from bullet import Bullet

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Admin\\Documents\\python projects\\Alien invasion game\\resources\\ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = 600
        self.speed = SHIP_SPEED
        self.bullet_delay = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        self.bullet_delay -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullets):
        if self.bullet_delay <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullets.add(bullet)
            self.bullet_delay = 30  # Adjust the delay as needed
