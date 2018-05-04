# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:33:31 2018
inicio do jogo - fit ninja
@author: vitoria
"""
import pygame
import sys
from pygame.locals import *
from random import randrange

class ComidaFit(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        #falta a função do movimento
    def move(self):
        self.rect.y += self.vy
        
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('Fit Ninja')

fundo = pygame.image.load("fundo.jpg").convert()
#falta rodar em uma lista de comidas, não só a agua
agua = ComidaFit("agua.png", randrange(400), -600, randrange(0,5),randrange(0,5))
agua_group = pygame.sprite.Group()
agua_group.add(agua)

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            
 # === SEGUNDA PARTE: LÓGICA DO JOGO ===
 #falta a looping principal do jogo
    agua.move()
     
 
     
 
    tela.blit(fundo, (0, 0))

    agua_group.draw(tela)

    pygame.display.update()

pygame.display.quit()