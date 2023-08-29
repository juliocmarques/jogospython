import pygame
import sys
import random

# Inicialize o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Números em Pygame")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações dos números
font = pygame.font.Font(None, 36)
numbers = []
number_rects = []

# Configurações de jogo
game_over = False

# Função para criar números aleatórios em locais aleatórios na tela
def create_random_number():
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    return x, y

current_number = 1

# Crie os números iniciais
for _ in range(10):
    x, y = create_random_number()
    numbers.append(current_number)
    number_rects.append(pygame.Rect(x, y, 50, 50))
    current_number += 1

current_number = 1


# Loop principal do jogo
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_number = None
            for i, rect in enumerate(number_rects):
                if rect.collidepoint(event.pos):
                    clicked_number = numbers[i]
                    break

            if clicked_number == current_number:
                current_number += 1

                # Remova o número clicado e crie um novo
                if current_number <= 10:
                    numbers.remove(clicked_number)
                    number_rects.remove(rect)
                else:
                    game_over = True


    screen.fill(WHITE)

    # Desenhe os números restantes
    for i, rect in enumerate(number_rects):
        pygame.draw.rect(screen, RED, rect)
        text = font.render(str(numbers[i]), True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 5))

    pygame.display.update()

# Encerre o Pygame
pygame.quit()
sys.exit()
