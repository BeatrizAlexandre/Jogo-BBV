# -- coding: utf-8 --
"""
Created on Fri May 11 08:49:15 2018

@author: biaku
"""

import pygame
from pygame.locals import *
from random import randrange


def text_objects(text, font):
    textSurface = font.render('Fit Ninja', True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects('Fit Ninja', largeText)
    TextRect.center = ((400),(100))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
    relogio.tick(15)

class Button(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()

    def setCords(self,x,y):
        self.rect.topleft = x,y

    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0] and \
            mouse[1] > self.rect.topleft[1] and \
            mouse[0] < self.rect.bottomright[0] and \
            mouse[1] < self.rect.bottomright[1]:
            return True
        else:
            return False


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


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Fit Ninja')
fundo_inicial = pygame.image.load("fundo.jpg").convert()

relogio = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

button = Button('button.png')
button.setCords(275,200)



fundo_inicial = pygame.image.load("fundo.jpg").convert()

largeText = pygame.font.Font('freesansbold.ttf',115)
TextSurf, TextRect = text_objects('Fit Ninja', largeText)
TextRect.center = ((400),(100))
fundo_inicial.blit(TextSurf, TextRect)
gameDisplay.blit(fundo_inicial, (0,0))
gameDisplay.blit(button.image, button.rect.topleft)
pygame.display.update()




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

fundo = pygame.image.load("fundo.jpg").convert()

estado = 0            

while estado != -1:
    
    relogio.tick(120)
    
    if estado == 0:  # Esperando começar o jogo.
        for event in pygame.event.get():
            if event.type == QUIT:
                estado = -1

            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.pressed(mouse_pos):
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
