import pygame
import os

largura = 800
altura = 600

# Configurações padrão
class configuracoes:
    def __init__(self):
        self.tela = pygame.display.set_mode((largura, altura))
        # Configuração do timer de renderização (FPS)
        self.clock = pygame.time.Clock()
        self.FPS = 60  # 60 quadros por segundo
        # Variável para controlar a reinicialização do jogo
        self.reiniciar_jogo = False
        # Pontuação
        self.pontuacao = 0

# Definir classe para o fundo
class Background:
    def __init__(self):
        # Carregar a imagem de fundo
        self.image = pygame.image.load(os.path.join("imagens", "background.png"))
        self.rect = self.image.get_rect()
        som_jogo = pygame.mixer.Sound("som/jogo.mp3")
        pygame.mixer.Sound.play(som_jogo)

# Definir classes para Personagem e Tartaruga
class Personagem:
    def __init__(self):
        # Inicializa o personagem
        self.image = pygame.image.load(os.path.join("imagens", "character.png"))
        self.rect = self.image.get_rect()
        self.x = 50
        self.y = altura - self.rect.height
        self.velocidade = 3
        self.gravidade = 0.3
        self.velocidade_pulo = 15
        self.pulando = False

    def mover(self, largura):
        # Move o personagem para a esquerda ou direita
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.x > self.velocidade:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.x < largura - self.rect.width - self.velocidade:
            self.x += self.velocidade

    def pular(self):
        # Faz o personagem pular
        if not self.pulando:
            self.pulando = True
            self.velocidade_y = self.velocidade_pulo
            som_pulo = pygame.mixer.Sound("som/pular.mp3")
            pygame.mixer.Sound.play(som_pulo)

    def aplicar_gravidade(self, altura):
        # Aplica a gravidade ao personagem enquanto ele está no ar
        if self.pulando:
            if self.velocidade_pulo >= -15:
                neg = 1
                if self.velocidade_pulo < 0:
                    neg = -1
                self.y -= (self.velocidade_pulo ** 2) * self.gravidade * neg

                teclas = pygame.key.get_pressed()
                # Ajuste da posição horizontal durante o pulo
                if teclas[pygame.K_LEFT] and self.x > self.velocidade:
                    self.x -= self.velocidade
                if teclas[pygame.K_RIGHT] and self.x < largura - self.rect.width - self.velocidade:
                    self.x += self.velocidade
                    
                self.velocidade_pulo -= 1
            else:
                self.pulando = False
                self.velocidade_pulo = 15
            # Verificar se o personagem está no chão
            if self.y >= altura - self.rect.height:
                self.y = altura - self.rect.height
                self.pulando = False

class Tartaruga:
    def __init__(self, largura):
        # Inicializa a tartaruga
        self.image = pygame.image.load(os.path.join("imagens", "turtle.png"))
        self.rect = self.image.get_rect()
        self.x = largura
        self.y = altura - self.rect.height
        self.velocidade = 3
        self.direcao = 1

    def mover(self, largura):
        # Move a tartaruga para a esquerda e direita na tela
        self.x += self.velocidade * self.direcao
        if self.x + self.rect.width > largura:
            self.direcao = -1
        elif self.x < 0:
            self.direcao = 1

class Colisao:
    @staticmethod
    def colisao_retangulos(rect1, rect2):
        """
        Verifica colisão entre dois retângulos.
        Retorna True se houver colisão, False caso contrário.
        """
        return rect1.colliderect(rect2)

    @staticmethod
    def colisao_quadrante_superior(personagem, tartaruga):
        """
        Verifica se o personagem colidiu com o quadrante superior da tartaruga.
        Retorna True se houver colisão, False caso contrário.
        """
        if (personagem.x + personagem.rect.width > tartaruga.x and
            personagem.x < tartaruga.x + tartaruga.rect.width and
            personagem.y + personagem.rect.height >= tartaruga.y and
            personagem.y < tartaruga.y):
            som_colisao_vertical = pygame.mixer.Sound("som/ganhou.mp3")
            personagem.image = pygame.image.load(os.path.join("imagens", "character_vertical.png"))
            tartaruga.image = pygame.image.load(os.path.join("imagens", "turtle_vertical.png"))
            pygame.mixer.Sound.play(som_colisao_vertical)
            return True        
        return False

    @staticmethod
    def colisao_lateral(personagem, tartaruga):
        """
        Verifica se o personagem colidiu com as laterais da tartaruga.
        Retorna True se houver colisão, False caso contrário.
        """
        if (personagem.x < tartaruga.x + tartaruga.rect.width
            and personagem.x + personagem.rect.width > tartaruga.x
            and personagem.y < tartaruga.y + tartaruga.rect.height
            and personagem.y + personagem.rect.height > tartaruga.y):
            som_colisao_horizontal = pygame.mixer.Sound("som/perdeu.mp3")        
            personagem.image = pygame.image.load(os.path.join("imagens", "character_horizontal.png"))
            tartaruga.image = pygame.image.load(os.path.join("imagens", "turtle_horizontal.png"))
            pygame.mixer.Sound.play(som_colisao_horizontal)

            return True
        return False
