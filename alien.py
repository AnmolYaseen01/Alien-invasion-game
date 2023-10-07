# alien.py
import pygame
import random
from settings import WIDTH, ALIEN_SPEED, ALIEN_RESPAWN_DELAY

class Alien(pygame.sprite.Sprite):
    spawn_delay = ALIEN_RESPAWN_DELAY

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Admin\\Documents\\python projects\\Alien invasion game\\resources\\alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, 0)
        self.speed = ALIEN_SPEED

    def update(self):
        self.rect.y += self.speed
