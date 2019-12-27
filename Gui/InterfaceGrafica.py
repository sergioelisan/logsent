'''
Created on 03/05/2011

@author: Serginho
'''

import pygame
import sys
from pygame.locals import *

from Widgets import Text, Image
from Cores import BLUBCC, GRAY, WHITE, BLACK
from Logic.Interpretadores import InferenceInterpreter, ExpressionInterpreter
from Util.Excessoes import InferenceRuleException

##
## Variaveis globais
##

surface = None
clock = None

##
## Funcoes de uso geral dos menus e interfaces
##

def shutdown():
    sys.exit()
      
        
def draw(surf, obj, x, y):
    ''' Funcao criada para desenhar um item na tela em uma determinada 
        posicao '''        
    rect = obj.get_rect() # Pega o retangulo desse item
    rect.topleft = (x, y)  # Insere as coordenadas x, y no canto supe-esquerdo
    surf.blit(obj, rect) # Insere o item sobre o retangulo posicionado
    
    
def updateScreen(spriteGroup):
    ''' Atualiza a tela'''
    surface.fill(WHITE)
    update(spriteGroup)
    
    
def update(*sprites):
    ''' Atualiza os Sprites da tela '''
    
    # Repinta os Sprites atualizados
    for sprite in sprites:
        sprite.draw(surface)

    pygame.display.update()

##
## Funcoes de avaliacao
##

def idenfity(premissas, conclusao):
    ''' Procura por uma inferencia e retorna seu nome. '''
    infInterpreter = InferenceInterpreter()
    expInterpreter = ExpressionInterpreter()
    
    _premissas = []
    for premissa in premissas:
        _premissas.append( expInterpreter.eval(premissa) )
    
    try:    
        q = expInterpreter.eval(conclusao)
        inference = infInterpreter.identify(_premissas, q)
        return inference.getRuleName()
    
    except InferenceRuleException as t:
        return str(t)


def complete(premissas, conclusao):
    pass



def proof(premissas, objetivo):
    pass


##
## Funcoes que desenham as interfaces do sistema
##

def init():
    pygame.init()
    
    global surface
    surface = pygame.display.set_mode( (800, 600), 0, 32)
    
    global clock 
    clock = pygame.time.Clock()
    pygame.display.set_caption("LogSent (R)")
    
    abertura()
    menu()
    
    
         
def abertura():
    background = pygame.image.load("__Images__/logo.png").convert()    
    surface.blit(background, (0, 0))
    
    pressEnter = Text(300, 520, 20, GRAY, "[ ENTER ] ou [ CLICK ]")
    update(pygame.sprite.Group(pressEnter))
    entered = False
    
    while not entered:
        clock.tick(3) 

        for event in pygame.event.get():    
            if event.type == QUIT:
                shutdown()
            elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                entered = True
                
                


def menu():
    ''' Interface de menu '''
    surface.fill(WHITE)
    selected = False
    
    txtIdentificador   = Text(45, 175, 30, GRAY, "  Identificador de R.I.  ")
    txtCompletar       = Text(45, 255, 30, GRAY, "  Completar R.I.  ")
    txtProvar          = Text(45, 335, 30, GRAY, "  Provar Argumentos  ")
    txtCreditos        = Text(45, 415, 30, GRAY, "  Creditos  ")
    
    title              = Image(25, 15, pygame.image.load("__Images__/logomarca.png").convert() )
    txtSubtitle        = Text (65, 110, 14, BLUBCC, "Who Inference Rule Is?")
    logo               = Image(465, 265, pygame.image.load("__Images__/logotipo.png").convert() )    

    opcoes = { 1 : identificar,
               2 : completar,
               3 : provar,
               4 : creditos }

    pos = { 
              1 : ( (txtIdentificador.rect.topleft[0] + 15, 
                     txtIdentificador.rect.bottomright[0] + 15),
                    (txtIdentificador.rect.topleft[1] + 15,
                     txtIdentificador.rect.bottomright[1] + 15) ),
                      
              2 : ( (txtCompletar.rect.topleft[0] + 15, 
                     txtCompletar.rect.bottomright[0] + 15),
                    (txtCompletar.rect.topleft[1] + 15,
                     txtCompletar.rect.bottomright[1] + 15) ),
                      
              3 : ( (txtProvar.rect.topleft[0] + 15, 
                     txtProvar.rect.bottomright[0] + 15),
                    (txtProvar.rect.topleft[1] + 15,
                     txtProvar.rect.bottomright[1] + 15) ),
                      
              4 : ( (txtCreditos.rect.topleft[0] + 15, 
                     txtCreditos.rect.bottomright[0] + 15),
                    (txtCreditos.rect.topleft[1] + 15,
                     txtCreditos.rect.bottomright[1] + 15) )
        }

    textos = pygame.sprite.Group(title,
                                 txtSubtitle, 
                                 txtIdentificador, 
                                 txtCompletar, 
                                 txtProvar,
                                 logo, 
                                 txtCreditos)
    while not selected:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                shutdown()
                
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                                
                ## Primeiro item do menu
                if (x >= pos[1][0][0] and x <= pos[1][0][1]) and \
                   (y >= pos[1][1][0] and y <= pos[1][1][1]):
                    opcoes[1]()                   
                
                ## Segundo item do menu
                elif (x >= pos[2][0][0] and x <= pos[2][0][1]) and \
                     (y >= pos[2][1][0] and y <= pos[2][1][1]):
                    opcoes[2]()
                
                ## Segundo item do menu
                elif (x >= pos[3][0][0] and x <= pos[3][0][1]) and \
                     (y >= pos[3][1][0] and y <= pos[3][1][1]):
                    opcoes[3]()
                
                ## Quarto item do menu
                elif (x >= pos[4][0][0] and x <= pos[4][0][1]) and \
                     (y >= pos[4][1][0] and y <= pos[4][1][1]):
                    opcoes[4]()

            elif event.type == MOUSEMOTION:
                x, y = event.pos
                                
                ## Primeiro item do menu
                if (x >= pos[1][0][0] and x <= pos[1][0][1]) and \
                   (y >= pos[1][1][0] and y <= pos[1][1][1]):                    
                    txtIdentificador.updateBackground(BLUBCC)
                    txtIdentificador.updateColor(WHITE)                      
                else:
                    txtIdentificador.updateBackground(WHITE)
                    txtIdentificador.updateColor(GRAY)
                
                ## Segundo item do menu
                if (x >= pos[2][0][0] and x <= pos[2][0][1]) and \
                   (y >= pos[2][1][0] and y <= pos[2][1][1]):
                    txtCompletar.updateBackground(BLUBCC)
                    txtCompletar.updateColor(WHITE)                      
                else:
                    txtCompletar.updateBackground(WHITE)
                    txtCompletar.updateColor(GRAY)
                    
                ## Terceiro item do menu
                if (x >= pos[3][0][0] and x <= pos[3][0][1]) and \
                   (y >= pos[3][1][0] and y <= pos[3][1][1]):
                    txtProvar.updateBackground(BLUBCC)
                    txtProvar.updateColor(WHITE)                      
                else:
                    txtProvar.updateBackground(WHITE)
                    txtProvar.updateColor(GRAY)
                    
                ## Quarto item do menu
                if (x >= pos[4][0][0] and x <= pos[4][0][1]) and \
                   (y >= pos[4][1][0] and y <= pos[4][1][1]):
                    txtCreditos.updateBackground(BLUBCC)
                    txtCreditos.updateColor(WHITE)                      
                else:
                    txtCreditos.updateBackground(WHITE)
                    txtCreditos.updateColor(GRAY)
                
        updateScreen(textos)









def identificar():
    ''' Interface de identificacao '''
    surface.fill(WHITE)
    exit  = False
    focus = None
    
    qntPremissas  = 1
    
    txtQUIT       = Text(765,  15,  20, BLUBCC, "X"                 )    
    title         = Text( 15,  15,  30,   GRAY, "Identifique a R.I.")    
    txtPremissas  = Text( 25,  80,  23,   GRAY, "Premissas"         )
    txtQuantidade = Text(150,  80,  23,  BLACK, str(qntPremissas)   )
    txtPlus       = Text(185,  75,  30, BLUBCC, "+"                 )
    txtMinus      = Text(220,  75,  30, BLUBCC, "-"                 )    
    txtResposta   = Text(450, 200,  30,  WHITE, None,        BLUBCC )    
    fieldP1       = Text( 75, 203,  23,   GRAY, " " * 30            )
    fieldP2       = Text( 75, 243,  23,   GRAY, " " * 30            )
    fieldP3       = Text( 75, 283,  23,   GRAY, " " * 30            )
    fieldQ        = Text( 75, 363,  23,   GRAY, " " * 30            )    
    txtP1         = Text( 25, 200,  25,  BLACK, "[1]"               )
    txtP2         = Text( 25, 240,  25,  BLACK, "[2]"               )
    txtP3         = Text( 25, 280,  25,  BLACK, "[3]"               )
    txtBar        = Text( 25, 320,  25,  BLACK, "-" * 25            )
    txtQ          = Text( 25, 360,  25,  BLACK, "[Q]"               )    
    txtOK         = Text( 95, 420,  30,  WHITE, "   OK   ",  BLUBCC )
    
    pos = {
           'quit'  : ((txtQUIT.rect.topleft[0] + 1,
                       txtQUIT.rect.bottomright[0] + 1),
                      (txtQUIT.rect.topright[1] + 1,
                       txtQUIT.rect.bottomleft[1] + 1)) ,
            
           'ok'    : ((txtOK.rect.topleft[0] + 1,
                       txtOK.rect.bottomright[0] + 1),
                      (txtOK.rect.topright[1] + 1,
                       txtOK.rect.bottomleft[1] + 1)) ,
                       
           'p1'    : ((txtP1.rect.topleft[0] + 1,
                       txtP1.rect.bottomright[0] + 1),
                      (txtP1.rect.topright[1] + 1,
                       txtP1.rect.bottomleft[1] + 1)) ,
                       
           'p2'    : ((txtP2.rect.topleft[0] + 1,
                       txtP2.rect.bottomright[0] + 1),
                      (txtP2.rect.topright[1] + 1,
                       txtP2.rect.bottomleft[1] + 1)) ,
                       
           'p3'    : ((txtP3.rect.topleft[0] + 1,
                       txtP3.rect.bottomright[0] + 1),
                      (txtP3.rect.topright[1] + 1,
                       txtP3.rect.bottomleft[1] + 1)) ,
            
           'f1'    : ((fieldP1.rect.topleft[0] + 1,
                       fieldP1.rect.bottomright[0] + 1),
                      (fieldP1.rect.topright[1] + 1,
                       fieldP1.rect.bottomleft[1] + 1)) ,
                       
           'f2'    : ((fieldP2.rect.topleft[0] + 1,
                       fieldP2.rect.bottomright[0] + 1),
                      (fieldP2.rect.topright[1] + 1,
                       fieldP2.rect.bottomleft[1] + 1)) ,
                       
           'f3'    : ((fieldP3.rect.topleft[0] + 1,
                       fieldP3.rect.bottomright[0] + 1),
                      (fieldP3.rect.topright[1] + 1,
                       fieldP3.rect.bottomleft[1] + 1)) ,
                       
           'fq'    : ((fieldQ.rect.topleft[0] + 1,
                       fieldQ.rect.bottomright[0] + 1),
                      (fieldQ.rect.topright[1] + 1,
                       fieldQ.rect.bottomleft[1] + 1)) ,
                       
           'bar'   : ((txtBar.rect.topleft[0] + 1,
                       txtBar.rect.bottomright[0] + 1),
                      (txtBar.rect.topright[1] + 1,
                       txtBar.rect.bottomleft[1] + 1)) ,
                       
           'q'     : ((txtQ.rect.topleft[0] + 1,
                       txtQ.rect.bottomright[0] + 1),
                      (txtQ.rect.topright[1] + 1,
                       txtQ.rect.bottomleft[1] + 1)) ,
                       
           'plus'  : ((txtPlus.rect.topleft[0] + 1,
                       txtPlus.rect.bottomright[0] + 1),
                      (txtPlus.rect.topright[1] + 1,
                       txtPlus.rect.bottomleft[1] + 1)) ,
                      
           'minus' : ((txtMinus.rect.topleft[0] + 1,
                       txtMinus.rect.bottomright[0] + 1),
                      (txtMinus.rect.topright[1] + 1,
                       txtMinus.rect.bottomleft[1] + 1))
          } 
    
    texts = pygame.sprite.Group( txtQUIT,     txtOK,
                                 title,       txtPremissas,   txtQuantidade,
                                 txtPlus,     txtMinus,       txtResposta,
                                 txtP1,       txtP2,          txtP3,  
                                 txtBar,      txtQ,           fieldP1,
                                 fieldP2,     fieldP3,        fieldQ )    
    while not exit:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                shutdown()
            
            elif event.type == KEYDOWN:  
                if focus != None:
                    if focus.msg == " " * 30 or focus.msg == "_": focus.msg = ''                        
                    if event.key == K_BACKSPACE:
                        focus.msg = focus.msg[:-1]
                        focus.updateMsg(focus.msg + '_')                        
                    else:
                        # Gambiarra, porque eu nao sei usar o SHIFT ainda ( _ _')
                        if event.key == K_PERIOD: focus.msg += unichr(K_GREATER)                                                        
                        elif event.key == K_COMMA: focus.msg += unichr(K_LESS)                        
                        elif event.key == K_1: focus.msg += unichr(K_EXCLAIM)  
                        elif event.key == K_2: focus.msg += "|"                      
                        elif event.key == K_7: focus.msg += unichr(K_AMPERSAND)                            
                        elif event.key == K_8: focus.msg += unichr(K_ASTERISK)                        
                        elif event.key == K_9: focus.msg += unichr(K_RIGHTPAREN)                            
                        elif event.key == K_0: focus.msg += unichr(K_LEFTPAREN)                        
                        else:                  focus.msg += unichr(event.key)
                                                    
                        focus.updateMsg(focus.msg + '_')
            
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                
                ## Botoes de incremento ou decremento de Premissas
                if (x >= pos['plus'][0][0] and x <= pos['plus'][0][1]) and \
                   (y >= pos['plus'][1][0] and y <= pos['plus'][1][1]) :
                    if qntPremissas < 3:
                        qntPremissas += 1
                        txtQuantidade.updateMsg( str(qntPremissas) )                        
                
                elif (x >= pos['minus'][0][0] and x <= pos['minus'][0][1]) and \
                     (y >= pos['minus'][1][0] and y <= pos['minus'][1][1]) :
                    if qntPremissas > 1:
                        qntPremissas -= 1
                        txtQuantidade.updateMsg( str(qntPremissas) )
                        
                ## Botao de SAIDA
                elif (x >= pos['quit'][0][0] and x <= pos['quit'][0][1]) and \
                     (y >= pos['quit'][1][0] and y <= pos['quit'][1][1]) :
                    exit = True                    
                    
                ## Botao OK
                elif (x >= pos['ok'][0][0] and x <= pos['ok'][0][1]) and \
                     (y >= pos['ok'][1][0] and y <= pos['ok'][1][1]) :
                    p1 = fieldP1.msg if fieldP1.msg != " " * 30 else None
                    p2 = fieldP2.msg if fieldP2.msg != " " * 30 else None
                    p3 = fieldP3.msg if fieldP3.msg != " " * 30 else None
                    q  = fieldQ.msg  if fieldQ.msg  != " " * 30 else None
                    
                    premissas = []
                    if qntPremissas == 1:
                        premissas = [p1]
                    elif qntPremissas == 2:
                        premissas = [p1, p2]
                    else:
                        premissas = [p1, p2, p3]
                        
                    txtResposta.updateMsg("  " + idenfity(premissas, q) + "  ")
                
                ## Campos de texto                
                if (x >= pos['f1'][0][0] and x <= pos['f1'][0][1]) and \
                   (y >= pos['f1'][1][0] and y <= pos['f1'][1][1]) :
                    focus = fieldP1
                    if focus.msg == " " * 30:
                        focus.msg = "_"
                                        
                elif (x >= pos['f2'][0][0] and x <= pos['f2'][0][1]) and \
                     (y >= pos['f2'][1][0] and y <= pos['f2'][1][1]) :
                    focus = fieldP2
                    if focus.msg == " " * 30:
                        focus.msg = "_"                    
                
                elif (x >= pos['f3'][0][0] and x <= pos['f3'][0][1]) and \
                     (y >= pos['f3'][1][0] and y <= pos['f3'][1][1]) :
                    focus = fieldP3
                    if focus.msg == " " * 30:
                        focus.msg = "_"                    
                    
                elif (x >= fieldQ.rect.topleft[0] + 1  and x <= fieldQ.rect.bottomright[0] + 1) and \
                     (y >= fieldQ.rect.topright[1] + 1 and y <= fieldQ.rect.bottomleft[1] + 1) :
                    focus = fieldQ
                    if focus.msg == " " * 30:
                        focus.msg = "_"
                                        
                else:
                    focus = None
                ## [END] Campos de texto
                
            elif event.type == MOUSEMOTION:
                x, y = event.pos
                
                if (x >= pos['plus'][0][0] and x <= pos['plus'][0][1]) and \
                   (y >= pos['plus'][1][0] and y <= pos['plus'][1][1]) :
                    txtPlus.updateColor(GRAY)
                else:
                    txtPlus.updateColor(BLUBCC)
                
                if (x >= pos['minus'][0][0] and x <= pos['minus'][0][1]) and \
                   (y >= pos['minus'][1][0] and y <= pos['minus'][1][1]) :
                    txtMinus.updateColor(GRAY)
                else:
                    txtMinus.updateColor(BLUBCC)
                    
                if (x >= pos['quit'][0][0] and x <= pos['quit'][0][1]) and \
                   (y >= pos['quit'][1][0] and y <= pos['quit'][1][1]) :
                    txtQUIT.updateBackground(BLUBCC)
                    txtQUIT.updateColor(WHITE)
                else:
                    txtQUIT.updateBackground(WHITE)
                    txtQUIT.updateColor(BLUBCC)
                    
                ## Campos de texto                
                if (x >= pos['f1'][0][0] and x <= pos['f1'][0][1]) and \
                   (y >= pos['f1'][1][0] and y <= pos['f1'][1][1]) :
                    fieldP1.updateBackground(WHITE)
                else:
                    if fieldP1.msg == " " * 30 or fieldP1.msg == '':                        
                        fieldP1.updateMsg(" " * 30)
                    
                if (x >= pos['f2'][0][0] and x <= pos['f2'][0][1]) and \
                   (y >= pos['f2'][1][0] and y <= pos['f2'][1][1]) :
                    fieldP2.updateBackground(WHITE)
                else:
                    if fieldP2.msg == " " * 30 or fieldP2.msg == '':                        
                        fieldP2.updateMsg(" " * 30)
                
                if (x >= pos['f3'][0][0] and x <= pos['f3'][0][1]) and \
                   (y >= pos['f3'][1][0] and y <= pos['f3'][1][1]) :
                    fieldP3.updateBackground(WHITE)
                else:
                    if fieldP3.msg == " " * 30 or fieldP3.msg == '':                        
                        fieldP3.updateMsg(" " * 30)
                    
                if (x >= fieldQ.rect.topleft[0] + 1  and x <= fieldQ.rect.bottomright[0] + 1) and \
                   (y >= fieldQ.rect.topright[1] + 1 and y <= fieldQ.rect.bottomleft[1] + 1) :
                    fieldQ.updateBackground(WHITE)
                else:
                    if fieldQ.msg == " " * 30 or fieldQ.msg == '':                        
                        fieldQ.updateMsg(" " * 30)
                ## [END] campos de texto
                              
        if qntPremissas == 1:
            if texts.has(txtP2):
                texts.remove(txtP2)
                texts.remove(fieldP2)           
            if texts.has(txtP3):
                texts.remove(txtP3) 
                texts.remove(fieldP3)               
            txtBar.rect  = Rect( (pos['p2'][0][0], pos['p2'][1][0], 
                                  pos['p2'][0][1], pos['p2'][1][1]) )            
            txtQ.rect    = Rect( (pos['p3'][0][0], pos['p3'][1][0], 
                                  pos['p3'][0][1], pos['p3'][1][1]) )
            fieldQ.rect  = Rect( (pos['f3'][0][0], pos['f3'][1][0], 
                                  pos['f3'][0][1], pos['f3'][1][1]) ) 
            
        elif qntPremissas == 2:
            if not texts.has(txtP2):
                texts.add(txtP2)
                texts.add(fieldP2)            
            if texts.has(txtP3):
                texts.remove(txtP3)
                texts.remove(fieldP3)               
            txtP2.rect   = Rect( (pos['p2'][0][0], pos['p2'][1][0], 
                                  pos['p2'][0][1], pos['p2'][1][1]) ) 
            fieldP2.rect = Rect( (pos['f2'][0][0], pos['f2'][1][0], 
                                  pos['f2'][0][1], pos['f2'][1][1]) )               
            txtBar.rect  = Rect( (pos['p3'][0][0], pos['p3'][1][0], 
                                  pos['p3'][0][1], pos['p3'][1][1]) )            
            txtQ.rect    = Rect( (pos['bar'][0][0], pos['bar'][1][0], 
                                  pos['bar'][0][1], pos['bar'][1][1]) )
            fieldQ.rect  = Rect( (pos['bar'][0][0] + 50, pos['bar'][1][0], 
                                  pos['bar'][0][1], pos['bar'][1][1]) )
            
        else:
            if not texts.has(txtP2):
                texts.add(txtP2)
                texts.add(fieldP2)
            if not texts.has(txtP3):
                texts.add(txtP3)
                texts.add(fieldP3)
            txtP2.rect   = Rect( (pos['p2'][0][0], pos['p2'][1][0], 
                                  pos['p2'][0][1], pos['p2'][1][1]) )
            txtP3.rect   = Rect( (pos['p3'][0][0], pos['p3'][1][0], 
                                  pos['p3'][0][1], pos['p3'][1][1]) )
            fieldP2.rect = Rect( (pos['f2'][0][0], pos['f2'][1][0], 
                                  pos['f2'][0][1], pos['f2'][1][1]) )
            fieldP3.rect = Rect( (pos['f3'][0][0], pos['f3'][1][0], 
                                  pos['f3'][0][1], pos['f3'][1][1]) )
            txtBar.rect  = Rect( (pos['bar'][0][0], pos['bar'][1][0], 
                                  pos['bar'][0][1], pos['bar'][1][1]) )            
            txtQ.rect    = Rect( (pos['q'][0][0], pos['q'][1][0], 
                                  pos['q'][0][1], pos['q'][1][1]) )
            fieldQ.rect  = Rect( (pos['fq'][0][0], pos['fq'][1][0], 
                                  pos['fq'][0][1], pos['fq'][1][1]) )
                          
        updateScreen(texts)  
                
        








def completar():
    print "Completar ainda nao implementado"







def provar():
    print "Provar ainda nao implementado"
    
    



def creditos():
    background = pygame.image.load("__Images__/logo.png").convert()    
    surface.blit(background, (0, 0))
    
    autor   = Text(300, 510, 20, GRAY, "[ Autor  ] Sergio Lisan")
    version = Text(300, 540, 20, GRAY, "[ Versao ] 1.3 GUI")
    
    update(pygame.sprite.Group(autor, version))
    entered = False
    
    while not entered:
        clock.tick(3) 

        for event in pygame.event.get():    
            if event.type == QUIT:
                shutdown()
            elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                entered = True



