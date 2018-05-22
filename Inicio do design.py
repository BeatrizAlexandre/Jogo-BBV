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



comidas = {
    'abacaxi': InfoComida(InfoComida.FIT, 'abacaxi.png', -1),
    'agua': InfoComida(InfoComida.FIT, 'agua.png', -1),
    'morango': InfoComida(InfoComida.FIT, 'morango.png', -1),
    'pessego': InfoComida(InfoComida.FIT, 'pessego.png', -1),
    'pizza': InfoComida(InfoComida.FAST_FOOD, 'pizza.png', 1),
    'burger': InfoComida(InfoComida.FAST_FOOD, 'burger.png', 1),
    'bacon': InfoComida(InfoComida.FAST_FOOD, 'bacon.png', 1)
}

lista_comidas = [
    'abacaxi', 'agua', 'morango', 'pessego', 'pizza', 'burger', 'bacon'
]


#Tela do jogo        
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

fast_food_group = pygame.sprite.Group()
comida_fit_group = pygame.sprite.Group()

for i in range(100):
    for c in lista_comidas:
        c = lista_comidas[randrange(len(lista_comidas))]
        rango = Comida(comidas[c].imagem, randrange(400), -600, 0, randrange(1,5),
                   comidas[c].recompensa)
        tipo_rango = comidas[c].tipo
        if tipo_rango == InfoComida.FAST_FOOD:
            fast_food_group.add(rango)
        elif tipo_rango == InfoComida.FIT:
            comida_fit_group.add(rango)

#Pontos
pontos = 0
font = pygame.font.SysFont("arial", 55)

#Vidas
vidas = 5
fonte = pygame.font.SysFont("arial", 55)

#Recorde
recorde = 0
fon= pygame.font.SysFont("arial", 55)

 # === SEGUNDA PARTE: LÓGICA DO JOGO ===
 #falta a looping principal do jogo

relogio = pygame.time.Clock()

pygame.mixer.music.load('Baby.mp3')


fundo = pygame.image.load("fundo.jpg").convert()

#TELAS
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
                    pygame.mixer.music.play(loops=-1,start=0.0)
                    estado = 1
        pygame.display.update()
                
    elif estado == 1:  # Jogo começa.
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                estado = -1
            elif events.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                bolinha.move(mouse_position[0], mouse_position[1])
        #destruindo comidas
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            fast_food_killed = pygame.sprite.spritecollide(bolinha, fast_food_group, True)
            comida_fit_killed = pygame.sprite.spritecollide(bolinha, comida_fit_group, True)
            for comida in fast_food_killed:
                pontos += comida.recompensa
                if pontos > recorde:
                    recorde = pontos
            for comida in comida_fit_killed:
                vidas += comida.recompensa
            if vidas < 0:
#                events.type = pygame.quit()
                estado = 0# TELA GAME OVER
            
    
        fast_food_group.update()
        comida_fit_group.update()
                
        tela.blit(fundo, (0, 0))
    
        tela.blit(bolinha.image, (bolinha.rect.x, bolinha.rect.y))
        
        #MOSTRA OS PONTOS NA TELA
        text = font.render("Pontos: {0}". format(pontos), True, (0, 1, 0))
        tela.blit(text, (580 - text.get_width() // 5, 120 - text.get_height() // 1))
        
        #MOSTRA AS VIDAS NA TELA
        texto = font.render("Vidas: {0}". format(vidas), True, (0, 1, 0))
        tela.blit(texto, (230 - texto.get_width() // 1, 120 - texto.get_height() // 1))
        
        fast_food_group.draw(tela)
        comida_fit_group.draw(tela)
    
        pygame.display.update()
        
    elif estado == 7:  #GAME OVER
        for event in pygame.event.get():
            if event.type == QUIT:
                estado = -1

            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.pressed(mouse_pos):
                    pygame.mixer.music.play(loops=-1,start=0.0)
                    estado = 1
        pygame.display.update()
#        

pygame.display.quit()
pygame.mixer.quit()
pygame.quit()