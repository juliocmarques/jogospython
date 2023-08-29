import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Tiro")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
preto = (0,0,0)

# Configurações da nave espacial
player_width = 130
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 5

# Configurações do projétil
projectile_width = 10
projectile_height = 30
projectile_x = 0
projectile_y = 0
projectile_speed = 10
projectile_state = "ready"  # "ready" para esperar, "fire" para atirar

# Configurações do inimigo
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = random.randint(50, 200)
enemy_speed = 2

# Configuração do timer de renderização (FPS)
clock = pygame.time.Clock()
FPS = 60  # 60 quadros por segundo

# Função para disparar um projétil
def fire_projectile(x, y):
    global projectile_state
    projectile_state = "fire"
    screen.blit(projectile_img, (x, y))

# Carregar imagens
background = pygame.image.load("imagens/background_nave.png")
player_img = pygame.image.load("imagens/player.png")
projectile_img = pygame.image.load("imagens/projectile.png")
enemy_img = pygame.image.load("imagens/enemy.png")

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed

    # Limitar a nave espacial dentro da tela
    player_x = max(-70, min(player_x, SCREEN_WIDTH - player_width + 30))

    # Disparar um projétil
    if keys[pygame.K_SPACE]:
        if projectile_state == "ready":
            projectile_x = player_x + player_width / 2 - projectile_width / 2
            projectile_y = player_y
            fire_projectile(projectile_x, projectile_y)

    # Movimento do projétil
    if projectile_state == "fire":
        projectile_y -= projectile_speed
        if projectile_y < 0: projectile_state = "ready"

    # Movimento do inimigo
    enemy_x += enemy_speed
    if enemy_x > SCREEN_WIDTH - enemy_width or enemy_x < 0: enemy_speed *= -1

    # Colisão entre projétil e inimigo
    if (
        enemy_x < projectile_x + projectile_width
        and enemy_x + enemy_width > projectile_x
        and enemy_y < projectile_y + projectile_height
        and enemy_y + enemy_height > projectile_y
    ):
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y = random.randint(50, 200)
        projectile_state = "ready"

    # Limpar a tela e desenhar o fundo apenas uma vez
    screen.fill(preto)
    screen.blit(background, (0, 0))

    # Controlar a taxa de quadros por segundo
    clock.tick(FPS)

    # Desenhe a nave espacial
    screen.blit(player_img, (player_x, player_y))

    # Desenhe o inimigo
    screen.blit(enemy_img, (enemy_x, enemy_y))

# **Adicione esta linha para desenhar o projétil**
    if projectile_state == "fire": screen.blit(projectile_img, (projectile_x, projectile_y))

    pygame.display.update()
