# -- coding: utf-8 --
"""
Created on Fri May 11 08:49:15 2018

@author: biaku
"""

<<<<<<< HEAD

=======
>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
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
    def _init_(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite._init_(self)
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
<<<<<<< HEAD
    def _init_(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite._init_(self)
=======
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def move(self, x, y):
        self.rect.x = x-10
        self.rect.y = y-10


<<<<<<< HEAD
=======

>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
bolinha = Mouse("bolinha.png", 0, 0)
bolinha_group = pygame.sprite.Group()
bolinha_group.add(bolinha)


<<<<<<< HEAD
=======

#cair os alimentos da lista Fast Food
for gordura in lisFast:
    if gordura == 'pizza':
        pizza = FastFood('pizza.png', randrange(400), -600, 1, randrange(1,5))
        pizza_group = pygame.sprite.Group()
        pizza_group.add(pizza)

    elif gordura == 'burger':
        burger = FastFood('burger.png', randrange(400), -600, 1, randrange(1,5))
        burger_group = pygame.sprite.Group()
        burger_group.add(burger)
    
    elif gordura == 'bacon':
        bacon = FastFood('bacon.png', randrange(400), -600, 1, randrange(1,5))
        bacon_group = pygame.sprite.Group()
        bacon_group.add(bacon)
    
>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
#cair os alimentos da lista fit:
for comida in listafit:
    if comida == 'agua':
        agua = ComidaFit("agua.png", randrange(400), -600, 1, randrange(1,2))
        agua_group = pygame.sprite.Group()
        agua_group.add(agua)
        
    elif comida == 'abacaxi':
        abacaxi = ComidaFit("abacaxi.png", randrange(400), -600, 1, randrange(1,2))
        abacaxi_group = pygame.sprite.Group()
        abacaxi_group.add(abacaxi)
        
    elif comida == 'morango':
        morango = ComidaFit("morango.png", randrange(400), -600, 1, randrange(1,2))
        morango_group = pygame.sprite.Group()
        morango_group.add(morango)
        
    elif comida == 'pessego':
        pessego = ComidaFit("pessego.png", randrange(400), -600, 1, randrange(1,2))
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

while True:
<<<<<<< HEAD
=======

>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
    agua.move()
    morango.move()
    abacaxi.move()
    pessego.move()
    
    
<<<<<<< HEAD
=======
    pizza.move1()
    bacon.move1()
    burger.move1()

>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
    for events in pygame.event.get():
        if events.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            bolinha.move(mouse_position[0], mouse_position[1])
    
<<<<<<< HEAD
    
=======

>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        if pygame.sprite.spritecollide(abacaxi, bolinha_group, False):
            abacaxi_group.remove(abacaxi)
        if pygame.sprite.spritecollide(morango, bolinha_group, False):
            morango_group.remove(morango)
        if pygame.sprite.spritecollide(agua, bolinha_group, False):
            agua_group.remove(agua)
        if pygame.sprite.spritecollide(pessego, bolinha_group, False):
<<<<<<< HEAD
            pessego_group.remove(pessego)    

            


 
=======
            pessego_group.remove(pessego)        

            
>>>>>>> 033ac5a17e735b7067b8913a9850200404f12b3c
    tela.blit(fundo, (0, 0))

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