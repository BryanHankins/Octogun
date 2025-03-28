import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, player):
        direction_vector = pygame.math.Vector2(player.rect.centerx - self.rect.centerx,
                                               player.rect.centery - self.rect.centery)
        if direction_vector.length() > 0:
            direction_vector = direction_vector.normalize()

        self.rect.x += direction_vector.x * ENEMY_SPEED
        self.rect.y += direction_vector.y * ENEMY_SPEED