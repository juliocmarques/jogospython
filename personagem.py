from options_personagem import *

# Inicialização do Pygame
pygame.init()

# Configurações da janela
pygame.display.set_caption("Mario Bros")

config = configuracoes()

# Ativar as configurações das imagens
personagem = Personagem()
tartaruga = Tartaruga(largura)
background = Background()

# Sons
pygame.mixer.init()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not config.reiniciar_jogo:
        # Movimentação do personagem
        personagem.mover(largura)
        personagem.aplicar_gravidade(altura)

        # Lógica do pulo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            personagem.pular()        
            
        tartaruga.mover(largura)

        colisao = Colisao()
        #Regra de Colisões
        if colisao.colisao_retangulos(personagem.rect, tartaruga.rect):
            if colisao.colisao_quadrante_superior(personagem, tartaruga):
                config.pontuacao += 1
                config.reiniciar_jogo = True                
            elif colisao.colisao_lateral(personagem, tartaruga):
                config.pontuacao -= 1
                config.reiniciar_jogo = True
    else:
        # Reiniciar o jogo após um tempo de espera
        pygame.time.delay(2000)  # 2000 ms = 2 segundos
        personagem = Personagem()
        tartaruga = Tartaruga(largura)
        config.reiniciar_jogo = False

    # Limpar a tela e desenhar o fundo apenas uma vez
    config.tela.fill((0,0,0)) #tela preta
    config.tela.blit(background.image, (0, 0))

    # Desenhar o personagem
    config.tela.blit(personagem.image, (personagem.x, personagem.y))

    # Desenhar a tartaruga
    config.tela.blit(tartaruga.image, (tartaruga.x, tartaruga.y))

    # Exibir a pontuação na tela
    fonte = pygame.font.Font(None, 36)
    texto_pontuacao = fonte.render(f'Pontuação: {config.pontuacao}', True, (255, 255, 255)) #cor da pontuação branco na tela
    config.tela.blit(texto_pontuacao, (10, 10))

    # Atualizar a tela
    pygame.display.update()

    # Controlar a taxa de quadros por segundo
    config.clock.tick(config.FPS)

# Encerrar o Pygame
pygame.quit()
