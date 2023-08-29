import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações padrão
class configuracoes_inicias():
        def __init__(self):             
            # Raquetes
            self.raquete_largura = 10
            self.raquete_altura = 100
            # Pontuação
            self.pontos_jogador1 = 0
            self.pontos_jogador2 = 0
            # Configurações da janela
            self.largura = 800
            self.altura = 600
            self.tela = pygame.display.set_mode((self.largura, self.altura))

# Configurações dos objetos
class Raquete1:
        def __init__(self):
            self.x = 50
            self.y = config.altura // 2 - config.raquete_altura // 2
            self.velocidade = 0

class Raquete2:
        def __init__(self):
            self.x = config.largura - 50 - config.raquete_largura
            self.y = config.altura // 2 - config.raquete_altura // 2
            self.velocidade = 0

class Bola:
        def __init__(self):
            self.x = config.largura // 2
            self.y = config.altura // 2
            self.velocidade_x = random.choice((1, -1))
            self.velocidade_y = random.choice((1, -1))
            self.raio = 20             

pygame.display.set_caption("Pong Simples")
config = configuracoes_inicias()
raquete1 = Raquete1()
raquete2 = Raquete2()
bola = Bola()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: raquete2.velocidade = -5
            elif event.key == pygame.K_DOWN: raquete2.velocidade = 5
            elif event.key == pygame.K_w: raquete1.velocidade = -5
            elif event.key == pygame.K_s: raquete1.velocidade = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: raquete2.velocidade = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s: raquete1.velocidade = 0

    # Movimentação das raquetes
    raquete1.y += raquete1.velocidade
    raquete2.y += raquete2.velocidade

    # Impedir que as raquetes saiam da tela
    raquete1.y = max(0, min(raquete1.y, config.altura - config.raquete_altura))
    raquete2.y = max(0, min(raquete2.y, config.altura - config.raquete_altura))

    # Movimentação da bola
    bola.x += bola.velocidade_x
    bola.y += bola.velocidade_y

    # Verificação de colisão com as raquetes
    if (raquete1.x < bola.x < raquete1.x + config.raquete_largura) and (raquete1.y < bola.y < raquete1.y + config.raquete_altura):
        bola.velocidade_x = abs(bola.velocidade_x)
    if (raquete2.x < bola.x < raquete2.x + config.raquete_largura) and (raquete2.y < bola.y < raquete2.y + config.raquete_altura):
        bola.velocidade_x = -abs(bola.velocidade_x)

    # Verificação de colisão com as bordas superior e inferior
    if bola.y <= 0 or bola.y >= config.altura: bola.velocidade_y = -bola.velocidade_y

    # Verificação de pontuação
    # atigiu o minimo da largura de tela (saiu do campo de visão)
    if bola.x < 0:
        config.pontos_jogador2 += 1
        bola = Bola()

    # atigiu o máximo da largura de tela (saiu do campo de visão)
    elif bola.x > config.largura:
        config.pontos_jogador1 += 1
        bola = Bola()

    # Limpar a tela
    config.tela.fill((0, 0, 0))

    # Desenhar raquetes e bola
    pygame.draw.rect(config.tela, (0, 0, 255), (raquete1.x, raquete1.y, config.raquete_largura, config.raquete_altura))
    pygame.draw.rect(config.tela, (0, 0, 255), (raquete2.x, raquete2.y, config.raquete_largura, config.raquete_altura))
    pygame.draw.circle(config.tela, (0, 0, 255), (bola.x, bola.y), bola.raio)

    # Mostrar pontuação
    fonte = pygame.font.Font(None, 36)
    texto_pontos = fonte.render(f"{config.pontos_jogador1} - {config.pontos_jogador2}", True, (0, 0, 255))
    config.tela.blit(texto_pontos, (config.largura // 2 - 50, 10))

    # Atualizar a tela
    pygame.display.update()

# Encerrar o Pygame
pygame.quit()
