# -*- coding: UTF-8 -*-

##
## Data:  23-04-2011
##

from Util.Util import cls, stop, creditos
import Eval.LogSentEval as LogSentEval
import Wiri.LogSentWiri as LogSentWiri

def main():
    creditos()
    sair = False    
    opcoes = {  '1' : LogSentEval.main,
                '2' : LogSentWiri.main,
                '3' : creditos }
    
    while not sair:
        cls()
        print " LogSent(R) Series"
        print
        print
        print
        print " + [S] Sair   ----- Selecione o Sistema -----    [3] Creditos +"
        print
        print
        print
        print 
        print "    [1] LogSent (EVAL)            [2] LogSent {W.I.R.I.}       "
        print
        print "    Statement Evaluator           Who Inference Rule Is?       "
        print
        print
        print
        print " + --- BCC Corporation 2011                                    "
        print
        print
        print
        
        choice = raw_input(" >> ")

        if choice in ['1', '2', '3']:
            action = opcoes[choice]
            action()
        
        elif choice in ['S', 's']:
            cls()
            print " + ----------------- +"
            print
            print "    Volte Sempre !!"
            print
            print " + ----------------- +"
            print
            sair = True
            raw_input()
    
        else:
            print
            print " [ERRO] Opcao invalida..."
            stop()
        
if __name__ == '__main__':
    main()