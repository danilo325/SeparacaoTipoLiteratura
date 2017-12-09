# -*- coding: utf-8 -*-
"""Z\
Created on Mon Nov  6 23:48:34 2017

@author: danilo
"""

from arvore import arvore
from no import no


from xml.dom.minidom import parse, parseString

arquivoXML = parse('teste//xml//t1.xml')
#arqivoGrade = open('teste//gradeDeEntidade//t1.txt','w')

def existeEm(lista,atributo,valor):
    for elemento in lista:
        if(elemento.attributes[atributo].value == valor):
            return True
    return False
    

sentencas = arquivoXML.getElementsByTagName('s')

print (len(sentencas))

print (sentencas[3].getElementsByTagName('graph')[0].attributes['root'].value)

nosInternos = sentencas[3].getElementsByTagName('nt')
arv = arvore(None)
for noInterno in nosInternos:
    natualP = no(noInterno,None)
    if(arv.getRoot()==None):
         arv.setRoot(natualP)
 
        
    linhas = noInterno.getElementsByTagName('edge')
    for linha in linhas:
        if(existeEm(nosInternos,xx))
        