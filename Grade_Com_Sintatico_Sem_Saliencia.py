'''
Created on 29/03/2013

@author: Marcio

Codigo onde o Objeto (Od e Op) tem prioridade sobre o Sujeito (S)

'''


#import glob
import os
import xml.etree.ElementTree as ET




def CriarGradeSin(ArqXML):
    ListaEntidades = [ ]
    VecSent = []
    VecIndSent =[]
    ListAtribPal = [[]]
    ListaPalSent =[[[]]]
    ListaANTid = []
    ListaCAT = []
    ListaIDrefs = [[]]
    ListaLABELS = [[]] 
    Sujeitos = []
    Objetos = []
    LemasListaEntidades = []
    LemasSujeitos = []
    LemasObjetos = []
    LemasOthersEntidades = []
    OthersEntidades = []


    doc = ET.parse(ArqXML)
    node0=doc.getroot()
    #node1=node0.find("corpus")
    node2=node0.find("body")
    for node in node2.getchildren():
        x=node.attrib["id"]
        VecIndSent.append(x)
        y=node.attrib["text"]    
        VecSent.append(y)
        node3=node.find("graph")
        for node4 in node3.getchildren():
            if node4.tag == 'terminals':
                for node5 in node4.getchildren():
                    temp=[]
                    temp.append(node5.attrib["id"])
                    temp.append(node5.attrib["word"])
                    temp.append(node5.attrib["lemma"])
                    temp.append(node5.attrib["pos"])
                    temp.append(node5.attrib["morph"])
                    temp.append(node5.attrib["extra"])
                    ListAtribPal.append(temp)
                ListaPalSent.append(ListAtribPal)
            if node4.tag=='nonterminals':
                for node6 in node4.getchildren():
                    temp=[]
                    temp1=[]
                    a=node6.attrib["id"]
                    b=node6.attrib["cat"]
                    ListaANTid.append(a)
                    ListaCAT.append(b)
                    for node7 in node6.getchildren():     #Procurando as Entidades de Sujeitos:                        
                        ad = node7.attrib["idref"] 
                        ae = node7.attrib["label"]                                      
                        temp.append(ad)
                        temp1.append(ae)
                    ListaIDrefs.append(temp)
                    ListaLABELS.append(temp1)                    
    del ListaIDrefs[0]
    del ListaLABELS[0]
                     
    for i in range(len(ListaIDrefs)):
        if ListaCAT[i] == 'np':
            for j in range(len(ListaLABELS[i])):
                if ListaLABELS[i][j]=='H':
                    idTemp = ListaIDrefs[i][j]
                    u = i-1
                    v = i                    
                    S = 0
                    while u >= 0:                        
                        if len(ListaIDrefs[u]) != 0:
                            for x in range(len(ListaIDrefs[u])):
                                if u < 0:
                                    break
                                elif ListaANTid[v]==ListaIDrefs[u][x]:  
                                    #if ListaLABELS[u][x]=='DN' or ListaLABELS[u][x]=='DP'or ListaLABELS[u][x]=='DNc':
                                        #X = X + 1
                                    if ListaLABELS[u][x]=='Od' or ListaLABELS[u][x]=='Op':
                                        for h in range(len(ListaPalSent[1])):
                                            g = h+1
                                            if g < len(ListaPalSent[1]):
                                                if ListaPalSent[1][g][0] == idTemp:
                                                    if ListaPalSent[1][g][3] == 'n' or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                                        Objetos.append(idTemp)
                                                        ListaEntidades.append(idTemp)
                                                        x = len(ListaIDrefs[u])
                                                        u = -1
                                                        break
                                                    else:
                                                        x = len(ListaIDrefs[u])
                                                        u = -1
                                                        break
                                    elif ListaLABELS[u][x]=='S':
                                        S = S + 1
                                        if ListaCAT[u-1] == 's':
                                            for h in range(len(ListaPalSent[1])):
                                                g = h+1
                                                if h < len(ListaPalSent[1]):
                                                    if ListaPalSent[1][g][0] == idTemp:
                                                        if ListaPalSent[1][g][3] == 'n'or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                                            Sujeitos.append(idTemp)
                                                            ListaEntidades.append(idTemp)
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break
                                                        else:
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break
                                        v = u                
                                    elif ListaCAT[u-1] == 's':
                                        if S == 0:
                                            for h in range(len(ListaPalSent[1])):
                                                g = h+1
                                                if g < len(ListaPalSent[1]):
                                                    if ListaPalSent[1][g][0] == idTemp:
                                                        if ListaPalSent[1][g][3] == 'n'or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                                            OthersEntidades.append(idTemp)
                                                            ListaEntidades.append(idTemp)
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break
                                                        else:
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break                                      
                                        else:
                                            for h in range(len(ListaPalSent[1])):
                                                g = h+1
                                                if h < len(ListaPalSent[1]):
                                                    if ListaPalSent[1][g][0] == idTemp:
                                                        if ListaPalSent[1][g][3] == 'n'or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                                            Sujeitos.append(idTemp)
                                                            ListaEntidades.append(idTemp)
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break
                                                        else:
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break
                                    elif ListaCAT[u] == 's':
                                        for h in range(len(ListaPalSent[1])):
                                                g = h+1
                                                if g < len(ListaPalSent[1]):
                                                    if ListaPalSent[1][g][0] == idTemp:
                                                        if ListaPalSent[1][g][3] == 'n'or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                                            OthersEntidades.append(idTemp)
                                                            ListaEntidades.append(idTemp)
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break
                                                        else:
                                                            x = len(ListaIDrefs[u])
                                                            u = -1
                                                            break                                        
                                    else:
                                        v = u
                            u = u - 1
                        else:                        
                            u = u - 1
        if ListaCAT[i] == 'fcl':
            for j in range(len(ListaLABELS[i])):
                if ListaLABELS[i][j]=='S':
                    idFcl = ListaIDrefs[i][j]
                    for h in range(len(ListaPalSent[1])-1):
                        g = h+1                 
                        if h < len(ListaPalSent[1]):
                            if ListaPalSent[1][g][0] == idFcl:
                                if ListaPalSent[1][g][3] == 'n' or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                    Sujeitos.append(idFcl)
                                    ListaEntidades.append(idFcl)

                elif ListaLABELS[i][j]=='Od' or ListaLABELS[i][j]=='Op':
                    idFcl2 = ListaIDrefs[i][j]
                    for h in range(len(ListaPalSent[1])-1):
                        g = h+1
                        if h < len(ListaPalSent[1]):
                            if ListaPalSent[1][g][0] == idFcl2:
                                if ListaPalSent[1][g][3] == 'n'or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                    Objetos.append(idFcl2)
                                    ListaEntidades.append(idFcl2)
                else:
                    idFcl3 = ListaIDrefs[i][j]
                    for h in range(len(ListaPalSent[1])-1):
                        g = h+1
                        if h < len(ListaPalSent[1]):
                            if ListaPalSent[1][g][0] == idFcl3:
                                if ListaPalSent[1][g][3] == 'n'or ListaPalSent[1][g][3] == 'prop' or ListaPalSent[1][g][3] == 'pron-pers':
                                    OthersEntidades.append(idFcl3)
                                    ListaEntidades.append(idFcl3)
                                                       
    '''
       Verificando se as entidades sao unicas
    '''                                                       
                              
    for j in range(len(ListaEntidades)):                              
        for i in range(len(ListaPalSent[1])):                                                                                                                                                                                               
            if i < (len(ListaPalSent[1]) - 1):                  #LEMA DAS ENTIDADES
                if ListaEntidades[j] == ListaPalSent[1][i+1][0]:
                    lema = ListaPalSent[1][i+1][2]    
                    LemasListaEntidades.append(lema)

    unicosLemasEnt = list(set(LemasListaEntidades))
    #print unicosLemasEnt
    
                                           
    for i in range(len(ListaPalSent[1])):                                                                                                                                                                                       
        for j in range(len(Sujeitos)):
            if i < (len(ListaPalSent[1]) - 1):                  #LEMA DAS ENTIDADES SUJEITOS
                if Sujeitos[j] == ListaPalSent[1][i+1][0]:
                    lema = ListaPalSent[1][i+1][2]    
                    LemasSujeitos.append(lema)

    for i in range(len(ListaPalSent[1])):                                                                                                                                                                                       
        for j in range(len(Objetos)):
            if i < (len(ListaPalSent[1]) - 1):                  #LEMA DAS ENTIDADES OBJETOS
                if Objetos[j] == ListaPalSent[1][i+1][0]:
                    lema = ListaPalSent[1][i+1][2]    
                    LemasObjetos.append(lema)
    for i in range(len(ListaPalSent[1])):                                                                                                                                                                                       
        for j in range(len(OthersEntidades)):
            if i < (len(ListaPalSent[1]) - 1):                  #LEMA DAS ENTIDADES DE OUTRAS FUNCOES SINTATICAS (X)
                if OthersEntidades[j] == ListaPalSent[1][i+1][0]:
                    lema = ListaPalSent[1][i+1][2]    
                    LemasOthersEntidades.append(lema)
                               
    for i in range(len(LemasObjetos)):
        for j in range(len(LemasOthersEntidades)):
            if LemasObjetos[i] == LemasOthersEntidades[j]:
                indice = Objetos[i].find('_')
                a = Objetos[i][1:indice]
                index = OthersEntidades[j].find('_')
                b = OthersEntidades[j][1:index]
                if a == b:
                    if j < len(OthersEntidades):
                        OthersEntidades[j] = '-'       #Retirando as Entidades repetidas com funcao sintatica de menor ordem
                        LemasOthersEntidades[j] = '-'                

    for i in range(len(LemasSujeitos)):
        for j in range(len(LemasObjetos)):
            if LemasSujeitos[i] == LemasObjetos[j]:
                indice = Sujeitos[i].find('_')
                a = Sujeitos[i][1:indice]
                index = Objetos[j].find('_')
                b = Objetos[j][1:index]
                if a == b:
                    Objetos[j] = '-'
                    LemasObjetos[j] = '-'
    '''
        Na declaracao da Grade

        j = coluna
        i = linha

    '''    
    Grade = [ [ '-' for j in range(len(unicosLemasEnt)+1) ] for i in range(len(VecSent)+1) ] 
  
    for i in range(len(VecSent)):     # linha
        for j in range(len(unicosLemasEnt)): # coluna
            Grade[0][j+1]= unicosLemasEnt[j]
        Grade[i+1][0] = i +1

    '''
        Preenchendo a Grade com Sujeito e Objetos
    '''          
    unicosLemasEnt = [''] + unicosLemasEnt

    for i in range(len(unicosLemasEnt)-1):
        i = i + 1
        if i < len(unicosLemasEnt):
            for j in range(len(ListaEntidades)):
                #if j <= (len(ListaEntidades)):
                    if unicosLemasEnt[i] == LemasListaEntidades[j]:
                        if unicosLemasEnt[i] in LemasSujeitos and ListaEntidades[j] in Sujeitos:
                            a = ListaEntidades[j].find('_')
                            b = ListaEntidades[j][1:a]
                            linha = int(b)
                            Grade[linha][i] = 'S'
                        elif unicosLemasEnt[i] in LemasObjetos and ListaEntidades[j] in Objetos:
                            a = ListaEntidades[j].find('_')
                            b = ListaEntidades[j][1:a]
                            linha = int(b)
                            Grade[linha][i] = 'O'
                        elif unicosLemasEnt[i] in LemasOthersEntidades and ListaEntidades[j] in OthersEntidades:
                            a = ListaEntidades[j].find('_')
                            b = ListaEntidades[j][1:a]
                            linha = int(b)
                            Grade[linha][i] = 'X'
                            
    return Grade       
                                       
'''
    Salvar a grade de entidade no arquivo 

'''   
def Salvar(nomeArq,Grade1):                       
    arq = open(nomeArq, 'w')
    for i in range(len(Grade1)-1):     # linha
        if i < len(Grade1):
            i = i +1
            for j in range(len(Grade1[0])-1):
                if j < len(Grade1[0]):
                    j = j + 1
                    arq.write(str(Grade1[i][j]))
            arq.write(str('\n'))
    arq.close()

def Carregar(nomeArq):
    arq = open(nomeArq, 'r')
    grade = []
    for linha in arq:
        grade.extend(grade.strip() for grade in linha.split('\n',))

    arq.close()
    return grade



x = os.listdir('teste/xml')
del x[0]

print (len(x))

for i in range(len(x)):
    j = i + 1
    
    w = x[i].find('.')
    w1 = x[i][:w]      
    
    print ("Para o Arquivo n."+str(j)+": "+x[i])
    Salvar('teste/gradeDeEntidade/'+w1+'_Grade.txt',CriarGradeSin('teste/xml/'+x[i]))
    print ("Terminado")
    falta = len(x) - i
'''
o = CriarGradeSin('D1_C31_Folha.txt.xml')
print o[0]
print '\n\n'
print o
#Salvar('GradeEnt/D1_C27_Folha_Grade.txt',CriarGradeSin('XML/D1_C27_Folha.txt.xml'))
#p = CriarGradeSin('XML/D1_C1_Folha.txt.xml')
#p =  Carregar('GradeEnt_O_S/D1_C38_Folha_Grade.txt')

for i in range(len(o)):
    print o[i]
'''

    
'''
print len(ListaEntidades)
print ListaEntidades
print '\n'

print LemasListaEntidades



print "Terminado"
print '\n'


print "++++++++++++++++++++++"

print "Entidades com Funcao Sintatica Sujeito"

print Sujeitos

print "++++++++++++++++++++++"

print "Entidades com Funcao Sintatica Sujeito"

print LemasSujeitos

print "++++++++++++++++++++++"

print "Entidades com Funcao Sintatica Objetos"

print LemasObjetos

print "++++++++++++++++++++++"

print "Entidades com Outras Funcoes Sintaticas"
print LemasOthersEntidades  
''' 