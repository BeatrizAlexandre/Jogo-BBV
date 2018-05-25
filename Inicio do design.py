# -- coding: utf-8 --
"""
Created on Fri May 11 08:49:15 2018

@author: vitoria
"""

import pygame
from pygame.locals import *
from random import randrange
from random import randint


def text_objects(text, font):
    textSurface = font.render('Fit Ninja', True, pink)
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
pink = (255,110,246)

config = Button('config.png')
config.setCords(100,400)

button = Button('button.png')
button.setCords(275,200)

music = Button ('music.png')
music.setCords(100,400)

replay = Button('replay.png')
replay.setCords(300,300)

sound = Button('sound.png')
sound.setCords(500,400)

fundo_inicial = pygame.image.load("fundo.jpg").convert()

largeText = pygame.font.Font('freesansbold.ttf',115)
TextSurf, TextRect = text_objects('Fit Ninja', largeText)
TextRect.center = ((400),(100))
fundo_inicial.blit(TextSurf, TextRect)
gameDisplay.blit(fundo_inicial, (0,0))
gameDisplay.blit(button.image, button.rect.topleft)
gameDisplay.blit(config.image, config.rect.topleft)
pygame.display.update()

bolinha = Mouse("bolinha.png", 0, 0)

fast_food_group = pygame.sprite.Group()
comida_fit_group = pygame.sprite.Group()

ultima_pos_y = 0
for i in range(randint(1,130)):
    c = lista_comidas[randrange(0,len(lista_comidas))]
    
    pos_x = randrange(0,600,130)
    pos_y = ultima_pos_y - randrange(200)
    ultima_pos_y = pos_y
    rango = Comida(comidas[c].imagem, pos_x, pos_y, 3, randrange(1,3),
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
#pygame.mixer.Sound('yay.wav')

fundo = pygame.image.load("fundo.jpg").convert()

right = pygame.image.load('right.png')
abacaxi = pygame.image.load('abacaxi.png')
agua = pygame.image.load('agua.png')
morango = pygame.image.load('morango.png')
pessego = pygame.image.load('pessego.png')
wrong = pygame.image.load('wrong.png')
pizza = pygame.image.load('pizza.png')
burger = pygame.image.load('burger.png')
bacon = pygame.image.load('bacon.png')

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
                elif config.pressed(mouse_pos):
                     gameDisplay.blit(fundo, (0,0))
                     estado = 2
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
                #pygame.mixer.Sound.play(1)
                pontos += comida.recompensa
#                if fast_food_killed not True:
#                    vidas -= comida.recompensa
            for comida in comida_fit_killed:
                vidas += comida.recompensa
            if vidas < 0:
                estado = 7  # TELA GAME OVER.
    
        fast_food_group.update()
        comida_fit_group.update()
        
        tem_comida = False
        for c in fast_food_group:
            if c.rect.y < 600:
                tem_comida = True
        for c in comida_fit_group:
            if c.rect.y < 600:
                tem_comida = True

        if not tem_comida:
            estado = 7
        
        tela.blit(fundo, (0, 0))
    
        tela.blit(bolinha.image, (bolinha.rect.x, bolinha.rect.y))
        
        #MOSTRA OS PONTOS NA TELA
        texto = font.render("Pontos: {0}". format(pontos), True, (0, 1, 0))
        tela.blit(texto, (580 - texto.get_width() // 5, 120 - texto.get_height() // 1))
        
        #MOSTRA AS VIDAS NA TELA
        texto = font.render("Vidas: {0}". format(vidas), True, (0, 1, 0))
        tela.blit(texto, (230 - texto.get_width() // 1, 120 - texto.get_height() // 1))
        
        fast_food_group.draw(tela)
        comida_fit_group.draw(tela)
    
        pygame.display.update()
        
    elif estado == 2:
        
        gameDisplay.blit(button.image, button.rect.topleft)
        gameDisplay.blit(music.image, music.rect.topleft)
        gameDisplay.blit(sound.image, sound.rect.topleft)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                estado = -1
                
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if music.pressed(mouse_pos):
                    pygame.mixer.quit()
                    estado = 3
                    
                elif sound.pressed(mouse_pos):
                    pygame.mixer.quit()
                    estado = 2
                
                elif button.pressed(mouse_pos):
                    pygame.mixer.music.play(loops=-1,start=0.0)
                    estado = 3
                    
        
                    
        pygame.display.update()
            
            
    elif estado == 3:
        gameDisplay.blit(fundo, (0,0))
        gameDisplay.blit(right, (225,100))
        gameDisplay.blit(agua, (50,300))
        gameDisplay.blit(abacaxi, (250,250))
        gameDisplay.blit(morango, (450,300))
        gameDisplay.blit(pessego, (650,300))
        texto = font.render("Não clique nas comidas fit!", True, pink)
        tela.blit(texto, (125,500))      
        pygame.display.update()        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                estado = -1
            elif events.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_SPACE]:
                    estado = 4        
    
    elif estado == 4:
        gameDisplay.blit(fundo, (0,0))
        gameDisplay.blit(wrong, (225,50))
        gameDisplay.blit(pizza, (75,250))
        gameDisplay.blit(burger, (300,250))
        gameDisplay.blit(bacon, (525,300))
        texto = font.render("Clique nos fast foods!", True, pink)
        tela.blit(texto, (125,450))
        text = font.render("Aperte espaço", True, pink)
        tela.blit (text, (300, 500))
        pygame.display.update()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                estado = -1
            elif events.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_SPACE]:
                    estado = 1
        
        
    elif estado == 7:  #GAME OVER
        tela.blit(fundo, (0, 0))
        Fonte= pygame.font.SysFont("freesansbold.ttf", 115)
        Fonte2= pygame.font.SysFont("freesansbold.ttf", 40)
        txt = Fonte.render("GAME OVER", True, (0, 1, 0))
        txt2 = Fonte2.render("REPLAY", True, (0, 0.2, 0))
        tela.blit(txt, (650 - txt.get_width() // 1, 200 - txt.get_height() // 1))
        #tela.blit(txt2, (650 - txt.get_width() // 1, 200 - txt.get_height() // 1))
        pygame.mixer.music.stop()

        tem_recorde = False

        for event in pygame.event.get():
            if event.type == QUIT:
                estado = -1
        
        if event.type == MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()
                if button.pressed(mouse_pos):
                    pygame.mixer.music.play(loops=-1,start=0.0)
                    estado = 1
                elif config.pressed(mouse_pos):
                     gameDisplay.blit(fundo, (0,0))
                     estado = 2



        if pontos > recorde:
            tem_recorde = True
            recorde = pontos

        while estado == 7:
            tela.blit(fundo, (0, 0))
            Fonte= pygame.font.SysFont("freesansbold.ttf", 115)
            txt = Fonte.render("GAME OVER", True, (0, 1, 0))
            tela.blit(txt, (650 - txt.get_width() // 1, 200 - txt.get_height() // 1))
            gameDisplay.blit(replay.image, replay.rect.topleft)
            tela.blit(txt2, (827 - txt.get_width() // 1, 455 - txt.get_height() // 1))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    estado = -1
                    
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if replay.pressed(mouse_pos):
                        pygame.mixer.music.play(loops=-1,start=0.0)
                        estado = 0
        

            if tem_recorde:
                texto = font.render("Novo Recorde: {0}". format(recorde), True, (0, 1, 0))
                tela.blit(texto, (550 - texto.get_width() // 1, 250 - texto.get_height() // 1))
            
            else:
                texto = font.render("Pontos: {0}". format(pontos), True, (0, 1, 0))
                tela.blit(texto, (500 - texto.get_width() // 1, 250 - texto.get_height() // 1))
            
            
              
            pygame.display.update()
        

pygame.display.quit()
pygame.mixer.quit()
pygame.quit()