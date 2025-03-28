import pygame, sys, random
from settings import *
from player import Player
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D 8-Directional Shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

player_group = pygame.sprite.GroupSingle()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player(WIDTH // 2, HEIGHT // 2)
player_group.add(player)

enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_event, ENEMY_SPAWN_RATE)

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == enemy_event:
            enemy_x = random.choice([random.randint(0, WIDTH), random.choice([-30, WIDTH + 30])])
            enemy_y = random.choice([random.randint(0, HEIGHT), random.choice([-30, HEIGHT + 30])])
            enemy_group.add(Enemy(enemy_x, enemy_y))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_group.add(player.shoot())

    player_group.update()
    enemy_group.update(player)
    bullet_group.update()

    for bullet in bullet_group:
        hits = pygame.sprite.spritecollide(bullet, enemy_group, True)
        if hits:
            bullet.kill()
            score += len(hits)

    if pygame.sprite.spritecollide(player, enemy_group, False):
        print(f"Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    player_group.draw(screen)
    enemy_group.draw(screen)
    bullet_group.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)