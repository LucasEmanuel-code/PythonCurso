import pygame
from pygame.locals import *

#tamanho da tela
Largura = 1000
Altura = 700

#Cores

D1 = (255,255,255)
D2 = (0,0,0)
D3 = (0,39,118)
D4 = (255,253,0)
D5 = (0,156,59)

def desenhar():

    pygame.draw.polygon(tela, D4, ((85, Altura/2), (Largura/2, 85), (Largura-85, Altura/2),(Largura/2, Altura-85)))
    pygame.draw.circle(tela, D3,(Largura/2, Altura/2), 175)
    pygame.draw.line(tela, D1, (330, 300), (666, 405), 11,)


tela = pygame.display.set_mode((Largura,Altura))

while True:
    tela.fill(D5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        desenhar()

        pygame.display.update()