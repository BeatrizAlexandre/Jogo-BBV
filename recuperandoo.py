# -*- coding: utf-8 -*-
"""
Created on Fri May 18 09:15:47 2018

@author: Beatriz
"""

import pygame
import sys
from pygame.locals import *
from random import randrange


class InfoComida:
    FAST_FOOD = 0
    FIT = 1    
    def __init__(self, tipo, imagem, recompensa):
        self.tipo = tipo
        self.imagem = imagem
        self.recompensa = recompensa
    def move(self, x, y):
        self.rect.x = x - 10
        self.rect.y = y - 10
     
        
comidas = {
    'abacaxi': InfoComida(InfoComida.FIT, 'abacaxi.png', 10),
    'agua': InfoComida(InfoComida.FIT, 'agua.png', 10),
    'morango': InfoComida(InfoComida.FIT, 'morango.png', 10),
    'pessego': InfoComida(InfoComida.FIT, 'pessego.png', 10),
    'pizza': InfoComida(InfoComida.FAST_FOOD, 'pizza.png', -10),
    'burger': InfoComida(InfoComida.FAST_FOOD, 'burger.png', -10),
    'bacon': InfoComida(InfoComida.FAST_FOOD, 'bacon.png', -10)
}

lista_comidas = [
    'abacaxi', 'agua', 'morango', 'pessego', 'pizza', 'burger', 'bacon'
]


#Tela        
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('Fit Ninja')

fundo = pygame.image.load("fundo.jpg").convert()

bolinha = Mouse("bolinha.png", 0, 0)


        
for c in lista_comidas:
    rango = Comida(comidas[c].imagem, randrange(400), -600, 0, randrange(1,5),
                   comidas[c].recompensa)
    tipo_rango = comidas[c].tipo
    if tipo_rango == InfoComida.FAST_FOOD:
        fast_food_group.add(rango)
    elif tipo_rango == InfoComida.FIT:
        comida_fit_group.add(rango)
        
 # === SEGUNDA PARTE: LÓGICA DO JOGO ===
 #falta a looping principal do jogo

relogio = pygame.time.Clock()

pygame.mixer.music.load('Baby.mp3')
pygame.mixer.music.play(loops=-1,start=0.0)

estado = 0            

while estado != -1:
    
    relogio.tick(120)
    
    if estado == 0:  # Esperando começar o jogo.
        for event in pygame.event.get():
            if event.type == QUIT:
                estado = -1

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    estado = 1
        pygame.display.update()
                
    elif estado == 1:  # Jogo começa.
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                estado = -1
            elif events.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                bolinha.move(mouse_position[0], mouse_position[1])
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            fast_food_killed = pygame.sprite.spritecollide(bolinha, fast_food_group, True)
            comida_fit_killed = pygame.sprite.spritecollide(bolinha, comida_fit_group, True)
    
        fast_food_group.update()
        comida_fit_group.update()
                
        tela.blit(fundo, (0, 0))
    
        tela.blit(bolinha.image, (bolinha.rect.x, bolinha.rect.y))
        
        fast_food_group.draw(tela)
        comida_fit_group.draw(tela)
    
        pygame.display.update()

pygame.display.quit()
pygame.mixer.quit()
pygame.quit()