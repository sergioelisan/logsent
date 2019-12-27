# -*- coding: UTF-8 -*-

from Logic.Interpretadores import ExpressionInterpreter, InferenceInterpreter
from Util.Excessoes import InferenceRuleException

# Interpretadores
exinterpreter = ExpressionInterpreter()
ri_interpreter = InferenceInterpreter()

# Regras de Inferencia
modusPonens     = ["!(!p -> !q) -> s", 
                   "!(!p -> !q)",
                   "s"]

modusTollens    = ["p -> !q", 
                   "q", 
                   "!p"]

silogismoHip    = ["p -> !q", 
                   "!q -> r", 
                   "p -> r"]

silogismoDis    = ["(a -> !b) | (b & !c)", 
                   "!(a -> !b)", 
                   "(b & !c)"]

adicao          = ["!(p <-> q)", 
                   "!(p <-> q) | r"]

simplificacao   = ["p & !(a -> b)", 
                   "p"]

conjuncao       = ["p", "!q", 
                   "p & !q"]

contraposicao   = ["!(p -> q) -> !s", 
                   "s -> (p -> q)"]

resolucao       = ["!p | q", 
                   " r | p", 
                   "q | r"]

dilemaCons      = ["p -> !q", 
                   "r -> !s", 
                   "p | r", 
                   "!q | !s"]

dilemaDes       = ["!p -> !q", 
                   "!r -> !s", 
                   "q | s", 
                   "p | r"] 

inferencias = [modusPonens, modusTollens, silogismoHip, silogismoDis, adicao, 
               simplificacao, conjuncao, contraposicao, resolucao, dilemaCons, 
               dilemaDes]

##
## Testes
##

def testIdentify():
    print " [TESTE] Identificacao de Regras de Inferencia\n\n"
     
    for rule in inferencias:
        premissas = []
        try:
            if len(rule) == 2:
                premissas.append(exinterpreter.eval(rule[0]) )
                
            elif len(rule) == 3:
                premissas.append(exinterpreter.eval(rule[0]) )
                premissas.append(exinterpreter.eval(rule[1]) )
                
            else:
                premissas.append(exinterpreter.eval(rule[0]) )
                premissas.append(exinterpreter.eval(rule[1]) )
                premissas.append(exinterpreter.eval(rule[2]) )
            
            conc = exinterpreter.eval(rule[-1])        
            inferencia = ri_interpreter.identify(premissas, conc)
            
            print " [", inferencia.nome, "] [ OK! ]\n", inferencia, "\n\n"
        
        except InferenceRuleException as t:
            print t       


    


def testaOQueAProfessoraQuer():
    print " [TESTE] Completar as Regras de Inferencia 2! O Retorno de Jaffar\n\n"
    
    a1 = exinterpreter.eval("(r & p) -> !q")
    a2 = exinterpreter.eval("!(!q)")    
    a_inference = ri_interpreter.complete([a1, a2])
    print a_inference.nome
    print a_inference
    print "\n"
    
    b1 = exinterpreter.eval("a -> (b -> c)")
    bc = exinterpreter.eval("!a")    
    b_inference = ri_interpreter.complete([b1, None], bc)
    print b_inference.nome
    print b_inference
    print "\n"
    
    c1 = exinterpreter.eval("(a & !b) | (b & !c)")
    cc = exinterpreter.eval("(a & !b)")
    c_inference = ri_interpreter.complete([c1, None], cc)
    print c_inference.nome
    print c_inference
    print "\n"
    
    d1 = exinterpreter.eval("!(!a -> !b) | c")
    d2 = exinterpreter.eval("!c")    
    d_inference = ri_interpreter.complete([d1, d2])
    print d_inference.nome
    print d_inference
    print "\n"
    
    e1 = exinterpreter.eval("a -> (b & c)")
    ec = exinterpreter.eval("a -> !d")
    e_inference = ri_interpreter.complete([e1, None], ec)
    print e_inference.nome
    print e_inference
    print "\n"




def testComplete():
    print " [TESTE] Completar as Regras de Inferencia\n\n"
        
    for rule in inferencias:
        if len(rule) == 2:
            print
            print
            p1 = exinterpreter.eval(rule[0])
            conclusao = exinterpreter.eval(rule[-1])
            
            try:
                inference = ri_interpreter.complete([None], conclusao)
                print " Faltando 1a premissa:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
            
            try:
                inference = ri_interpreter.complete([p1], None)
                print " Faltando conclusao:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
                
        elif len(rule) == 3:
            print
            print
            p1 = exinterpreter.eval(rule[0])
            p2 = exinterpreter.eval(rule[1])
            conclusao = exinterpreter.eval(rule[-1])
            
            try:
                inference = ri_interpreter.complete([None, p2], conclusao)
                print " Faltando 1a premissa:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
                
            try:
                inference = ri_interpreter.complete([p1, None], conclusao)
                print " Faltando 2a premissa:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
            
            try:
                inference = ri_interpreter.complete([p1, p2], None)
                print " Faltando conclusao:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
                        
        elif len(rule) == 4:
            print
            print
            p1 = exinterpreter.eval(rule[0])
            p2 = exinterpreter.eval(rule[1])
            p3 = exinterpreter.eval(rule[2])
            conclusao = exinterpreter.eval(rule[-1])
            
            try:
                inference = ri_interpreter.complete([None, p2, p3], conclusao)
                print " Faltando 1a premissa:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
            
            try:
                inference = ri_interpreter.complete([p1, None, p3], conclusao)
                print " Faltando 2a premissa:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
            
            try:
                inference = ri_interpreter.complete([p1, p2, None], conclusao)
                print " Faltando 3a premissa:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print
            
            try:
                inference = ri_interpreter.complete([p1, p2, p3], None)
                print " Faltando conclusao:", inference.nome, "OK!"
                print inference
                print
            except InferenceRuleException as t:
                print "", t, rule
                print






def testProof():
    print "\n [TESTE] Provar argumentos usando Regras de Inferencia\n"
    
    def printResults(logs, conclusao, obj):
        print "\n\n\n"    
        print " [OBJETIVO]", obj
        print 
        print " [RESPOSTA]"
        
        diference = len(conclusao) - len(logs)
        j = 0
        for i, premissa in enumerate(conclusao):
            if diference - 1 < i:
                string = " [ " + str(i) + " ] " + str(premissa)
                print string, " " * (30 - len(string)), logs[j]
                j += 1
            else:
                print " [", i, "]", premissa
    
    obj = exinterpreter.eval("r")    
    p1 = exinterpreter.eval("(p & t) -> (r | s)")
    p2 = exinterpreter.eval("q -> (u & t)")
    p3 = exinterpreter.eval("u -> p")
    p4 = exinterpreter.eval("!s")
    p5 = exinterpreter.eval("q")
    logs, conclusao = ri_interpreter.proof([p1, p2, p3, p4, p5], obj) 
    
    printResults(logs, conclusao, obj)
    
    obj = exinterpreter.eval("t")    
    p1 = exinterpreter.eval("!p & q")
    p2 = exinterpreter.eval("r -> p")
    p3 = exinterpreter.eval("!r -> s")
    p4 = exinterpreter.eval("s -> t")    
    logs, conclusao = ri_interpreter.proof([p1, p2, p3, p4], obj) 
    
    printResults(logs, conclusao, obj)
    
    obj = exinterpreter.eval("!t")    
    p1 = exinterpreter.eval("p -> s")
    p2 = exinterpreter.eval("p & q")
    p3 = exinterpreter.eval("(s & r) -> !t")
    p4 = exinterpreter.eval("q -> r")    
    logs, conclusao = ri_interpreter.proof([p1, p2, p3, p4], obj) 
    
    printResults(logs, conclusao, obj)
    
    obj = exinterpreter.eval("t & s")
    p1 = exinterpreter.eval("t -> s")
    p2 = exinterpreter.eval("!t -> !j")
    p3 = exinterpreter.eval("t & j")    
    logs, conclusao = ri_interpreter.proof([p1, p2, p3], obj)
    
    printResults(logs, conclusao, obj)
    
    obj = exinterpreter.eval("x+y=5")
    p1 = exinterpreter.eval("3x+y=11 <-> 3x=9")
    p2 = exinterpreter.eval("(3x=9 -> 3x+y=11) <-> y=2")
    p3 = exinterpreter.eval("!(y=2) | x+y=5")    
    logs, conclusao = ri_interpreter.proof([p1, p2, p3], obj)
    
    printResults(logs, conclusao, obj)
    
    obj = exinterpreter.eval("s")
    p1 = exinterpreter.eval("p -> (q & r)")
    p2 = exinterpreter.eval("p")
    p3 = exinterpreter.eval("t -> !q")
    p4 = exinterpreter.eval("t | s")    
    logs, conclusao = ri_interpreter.proof([p1, p2, p3, p4], obj)
    
    printResults(logs, conclusao, obj)
    
    
    
    
    
    
    

def testNewEval():
    s1 = "p -> q"
    s2 = "!(p -> r)"
    s3 = "!p | !q"
    s4 = "!(p & r) -> !s"
    s5 = "!p -> (p <-> (!q | p))"
    
    expinterpreter = ExpressionInterpreter()
    
    e1 = expinterpreter.eval(s1)
    print e1
    
    e2 = expinterpreter.eval(s2)
    print e2
    
    e3 = expinterpreter.eval(s3)
    print e3
    
    e4 = expinterpreter.eval(s4)
    print e4
    
    e5 = expinterpreter.eval(s5)
    print e5
    
    
    
    
    
    
    
    
    
    
    
    
    
# "Testinhos..." ...como diz a professora de Calculo

testNewEval()
testIdentify() #OK!
testComplete() #OK!
testaOQueAProfessoraQuer() #OK!
testProof() #OK!
