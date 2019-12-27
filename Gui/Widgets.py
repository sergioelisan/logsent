'''
Created on 03/05/2011

@author: Serginho
'''
import pygame
from Cores import WHITE


class Image(pygame.sprite.Sprite):
    ''' Sprite de uma imagem'''
    
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.update(x, y, img)        

    def update(self, x, y, img):
        ''' Atualiza os dados de alerta '''
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        

class Text(pygame.sprite.Sprite):
    ''' Sprite que eh a representacao grafica de um texto '''
    
    def __init__(self, x, y, font_size, textColor, mensagem, bg = WHITE):
        pygame.sprite.Sprite.__init__(self)
        self.textColor  = textColor
        self.background = bg
        self.msg   = mensagem
        self.font  = pygame.font.Font("Gui/__Fonts__/ubuntu.ttf", font_size)
        self.image = self.font.render(mensagem, True, self.textColor, bg)
        self.rect  = self.image.get_rect()
        self.rect.topleft = (x, y)

    def updateMsg(self, msg, fg = None, bg = None):
        ''' Atualiza os dados de alerta '''
        if fg == None:         
            fg = self.textColor
        if bg == None:  
            bg = self.background
                    
        self.image = self.font.render(msg, True, fg, bg)

    def updateColor(self, fg):
        ''' Atualiza apenas as cores do texto '''
        self.textColor = fg
        self.updateMsg(self.msg, fg = fg)

    def updateBackground(self, bg):
        ''' Atualiza a textColor de fundo do texto '''
        self.background = bg            
        self.updateMsg(self.msg, bg = bg)



    
    