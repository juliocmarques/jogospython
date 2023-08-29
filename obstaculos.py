import pygame
import random
import sys

pygame.init()

# Configurações da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo Simples com Pygame")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurações do jogador
player_width = 50
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 5

# Configurações dos obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
obstacle_y = 0
obstacle_speed = 3

# Variável para controlar o estado do jogo
game_over = False

# Variável para controlar o aumento de velocidade dos obstáculos
obstacle_speed_increase = 0.1

# Loop principal do jogo
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed

    # Atualize a posição do obstáculo
    obstacle_y += obstacle_speed

    # Verifique se o obstáculo saiu da tela
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
        obstacle_y = 0
        obstacle_speed += obstacle_speed_increase

    # Verifique a colisão entre o jogador e o obstáculo
    if (
        player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x
        and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y
    ):
        game_over = True

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    pygame.display.update()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

