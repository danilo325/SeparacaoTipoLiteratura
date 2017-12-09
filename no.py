# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 00:51:26 2017

@author:  Danilo Martins Silvério Cardoso

"""

class no:
    '''
        Função de inicilaização da classe
        Todo o objeto criado com esta classe terá estes elementos inicializados
    '''
    def __init__(self, dado,pai):
        self.dado = dado #verificar se o dado será equivalente a palavra
        self.pai = pai
        self.filhos = []
        self.cat = None
        self.label=None #O label define qual será o tipo da conexão entre o nó e seupai.
        self.linha=None
        self.identi = None
        
    '''
        Metodo que retorna o dado presente no nó
    '''    
    def getDado(self):
        return self.dado

    def getCat(self):
        return self.cat

    def setCat(self,cat):
        self.cat=cat

    def getLabel(self):
        return self.label

    def setLabel(self,label):
        self.label=label
    def getIdenti(self):
        return self.identi
    def setIdenti(self,indent):
        self.identi = indent
        
        

    '''
        Metodo que permite alterar o dado prestente no nó
    '''
    def setDado(self,dado):
        self.dado = dado
        
    '''
        Metodo que retorna o no pai.(Se for o no root ele não terá pai)
    '''
    def getPai(self):
        return self.pai
    '''
        Metodo que permite alterar o no pai
    '''
    def setPai(self,pai):
        self.pai = pai
        
    '''
        Metodo que retorna a lista de nos filhos
    '''    
    def getFilhos(self):
        return self.filhos
    '''
        Metodo que permite alterar a lista de nos filhos
    '''    
    def setFilhos(self,filhos):
        self.filhos = filhos
        
    def verificaSeRoot(self):
        return self.pai!=None
            
    def adcionaFilho(self,novofilho):
        self.filhos.append(novofilho)
        
'''    def removeFilho(self,filhoremover):
       if filhoremover.verificaSeRoot():
           
           
       paifilhoremovido = filhoremover.getPai()
       
       for filho in filhoremover.getFilhos():
           paifilhoremovido.getFihlos().append(filho)
           
       self.filhos.remove(filhoremover)
       
   '''     
        
