import pygame
from settings import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = pygame.math.Vector2(1, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            dx += PLAYER_SPEED
        if keys[pygame.K_UP]:
            dy -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            dy += PLAYER_SPEED

        if dx != 0 or dy != 0:
            self.direction = pygame.math.Vector2(dx, dy).normalize()

        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def shoot(self):
        return Bullet(self.rect.centerx, self.rect.centery, self.direction)