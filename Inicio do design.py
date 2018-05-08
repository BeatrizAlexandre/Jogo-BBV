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

listafit = ['abacaxi', 'agua', 'morango', 'pessego']

class ComidaFit(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def move(self):
        self.rect.y += self.vy
        
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('Fit Ninja')

fundo = pygame.image.load("fundo.jpg").convert()


#cair os alimentos da lista fit:
for comida in listafit:
    if comida == 'agua':
        agua = ComidaFit("agua.png", randrange(400), -600, randrange(0,5),randrange(0,5))
        agua_group = pygame.sprite.Group()
        agua_group.add(agua)
        
    elif comida == 'abacaxi':
        abacaxi = ComidaFit("abacaxi.png", randrange(400), -600, randrange(0,5),randrange(0,5))
        abacaxi_group = pygame.sprite.Group()
        abacaxi_group.add(abacaxi)
        
    elif comida == 'morango':
        morango = ComidaFit("morango.png", randrange(400), -600, randrange(0,5),randrange(0,5))
        morango_group = pygame.sprite.Group()
        morango_group.add(morango)
        
    elif comida == 'pessego':
        pessego = ComidaFit("pessego.png", randrange(400), -600, randrange(0,5),randrange(0,5))
        pessego_group = pygame.sprite.Group()
        pessego_group.add(pessego)
        


rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            
 # === SEGUNDA PARTE: LÓGICA DO JOGO ===
 #falta a looping principal do jogo
    agua.move()
    abacaxi.move()
    morango.move()  
    pessego.move()

     
 
    tela.blit(fundo, (0, 0))

    agua_group.draw(tela)
    abacaxi_group.draw(tela)
    morango_group.draw(tela)
    pessego_group.draw(tela)

    pygame.display.update()

pygame.display.quit()