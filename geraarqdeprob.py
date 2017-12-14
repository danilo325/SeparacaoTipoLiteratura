# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:17:20 2017

@author: danilo.cardoso
"""
import os


def Probabilidade(nomeArquivo):
    print('Criando vetor de probablidade para'+nomeArquivo+'\n')
    grade = open('teste/gradeDeEntidade/'+nomeArquivo)
    
    
    dicionarioValores = {'--':0,'-S':0,'-X':0,'-O':0,'SS':0,
    'S-':0,'SX':0,'SO':0,'XX':0,'X-':0,'XS':0,'XO':0,'OO':0,'O-':0,'OX':0,'OS':0}
    dicionarioProbablilidade = {'--':0,'-S':0,'-X':0,'-O':0,'SS':0,
    'S-':0,'SX':0,'SO':0,'XX':0,'X-':0,'XS':0,'XO':0,'OO':0,'O-':0,'OX':0,'OS':0}
    print (dicionarioValores)
    linhasDaGrade = grade.readlines()
    print(linhasDaGrade)
    QtdColunasGrade = len(linhasDaGrade[0])
    QtdLinhasGrade = len(linhasDaGrade)
    for j in range(QtdColunasGrade):
        for i in range(QtdLinhasGrade):
            if(i+1<QtdLinhasGrade and linhasDaGrade[i][j]!= '\n'):
                chave =(linhasDaGrade[i][j]+linhasDaGrade[i+1][j])            
                dicionarioValores[chave]=dicionarioValores[chave]+1
    soma =0
    for chave in dicionarioValores:
        soma = soma + dicionarioValores[chave]
        
    linhaChave =''
    linhaValores =''                            
    for key in dicionarioValores:
        dicionarioProbablilidade[key] = (dicionarioValores[key]/soma)*100
        linhaChave =linhaChave+'| '+key+' |'
        linhaValores =linhaValores+'|'+str(dicionarioProbablilidade[key])+'|'
                                                  
    arquivoProb = open('teste/prob/Prob_'+nomeArquivo,'w')
    #arquivoProb.write(linhaChave+'\n')
    arquivoProb.write(linhaValores)
    
        
        
    print(dicionarioProbablilidade)
    
       
    
    arquivoProb.close()
    grade.close()
    print('Vetor de Probabilidade do arquivo '+ nomeArquivo+' criada\n')
    
pastaDeArquivo = os.listdir('teste/gradeDeEntidade')
for nomeArquivo in pastaDeArquivo:
    Probabilidade(nomeArquivo)
