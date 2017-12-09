# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:30:38 2017

@author: danilo
"""

class arvore:
    arv=''
    
    def __init__(self,root):
        self.root = root
        
    def arvoreRecur(self,no):    
        self.arv+=no.getDado()     
        for filho in no.getFilhos():
           self.arvoreRecur(filho)
           
        return self.arv
        
        
    def imprimeArqvore(self):
        arvore = ""
        if(self.root == None):
            arvore += 'X'
        else:            
            return self.arvoreRecur(self.root)   

