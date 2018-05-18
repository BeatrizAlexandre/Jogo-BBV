# -- coding: utf-8 --
"""
Created on Fri May 11 08:49:15 2018

@author: biaku
"""

import pygame
from pygame.locals import *
from random import randrange

listafit = ['abacaxi', 'agua', 'morango', 'pessego']
imagens_listafit = {
    'abacaxi': 'abacaxi.png',
    'agua': 'agua.png',
    'morango': 'morango.png',
    'pessego': 'pessego.png'
}

lisFast = ['pizza', 'burger', 'bacon']
imagens_lisFast = {
    'pizza': 'pizza.png',
    'burger': 'burger.png',
    'bacon': 'bacon.png'
}

#classe das comidas que SUBTRAEM pontos
class Comida(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y, recompensa):
        pygame.sprite.Sprite.__init__(self)
        self.recompensa = recompensa
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        self.rect.y += self.vy

#mexer o mouse
class Mouse(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def move(self, x, y):
        self.rect.x = x - 10
        self.rect.y = y - 10

#Tela        
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('Fit Ninja')

fundo = pygame.image.load("fundo.jpg").convert()

bolinha = Mouse("bolinha.png", 0, 0)

#cair os alimentos da lista Fast Food
fast_food_group = pygame.sprite.Group()

for gordura in lisFast:
    fast = Comida(imagens_lisFast[gordura], randrange(400), -600, 1, 
                  randrange(1,5), -10)
    fast_food_group.add(fast)
    
#cair os alimentos da lista fit:
comida_fit_group = pygame.sprite.Group()
        
for comida in listafit:
    fit = Comida(imagens_listafit[comida], randrange(400), -600, 1, 
                 randrange(1,2), 10)
    comida_fit_group.add(fit)
        
#usar randint

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
