# -*- coding: UTF-8 -*-

##
## Data:  24-04-2011
##

from os import system

def creditos():
    ''' Exibe os creditos do sistema '''
    cls()
    print "    KK                         KKKKKK                           (R)"
    print "    KK       KKKKKK   KKKKK   KK        KKKKKK KKK  KK KKKKKKKK    "
    print "    KK      KK    KK KK        KKKKK   KK      KKKK KK    KK       "
    print "    KK      KK    KK KK  KKK       KK  KKKKK   KK KKKK    KK       "
    print "    KK      KK    KK KK   KK       KK  KK      KK  KKK    KK       "
    print "    KKKKKKK  KKKKKK   KKKKK   KKKKKK    KKKKKK KK   KK    KK       "
    print
    print
    print "                 Logic Senteces. Criando Logica no Caos!"
    print " + ------------------------------------------------------------- + "
    print
    print
    print "              (C)2011. Todos os direitos reservados.               "
    print
    print " [VERSAO]   1.2                                                    "
    print 
    print " [ENTERPRISE]  BCC Corporation Empire, 2011                        "
    stop()

def cls():
    ''' Limpa a tela '''
    system("cls")
    print

def stop():
    ''' Para a execucao esperando por uma acao do usuario'''
    print
    raw_input(" [ENTER] Continuar...")
