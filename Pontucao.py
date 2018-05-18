# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:37:40 2018

@author: Beatriz
"""


import pygame
import sys
from pygame.locals import *
from random import randrange

listafit = ['abacaxi', 'agua', 'morango', 'pessego']
lisFast = ['pizza', 'burger', 'bacon']



class FastFood(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def move1(self):
        self.rect.y += self.vy

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




#mexer o mouse
class Mouse(pygame.sprite.Sprite):


    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def move(self, x, y):
        self.rect.x = x-10
        self.rect.y = y-10



bolinha = Mouse("bolinha.png", 0, 0)
bolinha_group = pygame.sprite.Group()
bolinha_group.add(bolinha)



#cair os alimentos da lista Fast Food
for gordura in lisFast:
    if gordura == 'pizza':
        pizza = FastFood('pizza.png', randrange(400), -600, 1, randrange(2,4))
        pizza_group = pygame.sprite.Group()
        pizza_group.add(pizza)

    elif gordura == 'burger':
        burger = FastFood('burger.png', randrange(400), -600, 1, randrange(2,4))
        burger_group = pygame.sprite.Group()
        burger_group.add(burger)
    
    elif gordura == 'bacon':
        bacon = FastFood('bacon.png', randrange(400), -600, 1, randrange(2,4))
        bacon_group = pygame.sprite.Group()
        bacon_group.add(bacon)
    

#cair os alimentos da lista fit:
for comida in listafit:
    if comida == 'agua':
        agua = ComidaFit("agua.png", randrange(400), -600, 1, randrange(2,4))
        agua_group = pygame.sprite.Group()
        agua_group.add(agua)
        
    elif comida == 'abacaxi':
        abacaxi = ComidaFit("abacaxi.png", randrange(400), -600, 1, randrange(2,4))
        abacaxi_group = pygame.sprite.Group()
        abacaxi_group.add(abacaxi)
        
    elif comida == 'morango':
        morango = ComidaFit("morango.png", randrange(400), -600, 1, randrange(2,4))
        morango_group = pygame.sprite.Group()
        morango_group.add(morango)
        
    elif comida == 'pessego':
        pessego = ComidaFit("pessego.png", randrange(400), -600, 1, randrange(2,4))
        pessego_group = pygame.sprite.Group()
        pessego_group.add(pessego)
        
#usar randint

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            quit()
            
 # === SEGUNDA PARTE: LÓGICA DO JOGO ===
 #falta a looping principal do jogo
 
#pontos

ponto = Mouse("pontos.png", 0, 0)
ponto_group = pygame.sprite.Group()
ponto_group.add(ponto)

pontos = 0

font = pygame.font.SysFont("comicsansms", 72)


while True:

    morango.move()
    abacaxi.move()
    pessego.move()
    

    pizza.move1()
    bacon.move1()
    burger.move1()

    for events in pygame.event.get():
        if events.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            bolinha.move(mouse_position[0], mouse_position[1])

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        #DESTRUINDO COMIDAS FIT
        if pygame.sprite.spritecollide(abacaxi, bolinha_group, False):
            abacaxi_group.remove(abacaxi)
        if pygame.sprite.spritecollide(morango, bolinha_group, False):
            morango_group.remove(morango)
        if pygame.sprite.spritecollide(agua, bolinha_group, False):
            agua_group.remove(agua)
        if pygame.sprite.spritecollide(pessego, bolinha_group, False):
            pessego_group.remove(pessego)
        #DESTRUINDO FAST FOOD
        if pygame.sprite.spritecollide(pizza, bolinha_group, False):
            pizza_group.remove(pizza)
            pontos += 1
        if pygame.sprite.spritecollide(bacon, bolinha_group, False):
            bacon_group.remove(bacon)
            pontos += 1
        if pygame.sprite.spritecollide(burger, bolinha_group, False):
            burger_group.remove(burger)
            pontos += 1
    
    text = font.render("Pontos: {0}". format(pontos), True, (0, 1, 0))

    tela.blit(fundo, (0, 0))
    tela.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    agua_group.draw(tela)
    abacaxi_group.draw(tela)
    morango_group.draw(tela)
    pessego_group.draw(tela)
    bolinha_group.draw(tela)
    

    bolinha_group.draw(tela)
    
    
    pizza_group.draw(tela)
    bacon_group.draw(tela)
    burger_group.draw(tela)


    pygame.display.update()
    
pygame.display.quit()