# -*- coding: utf-8 -*- 
#Programa le arquivo xml
#Danilo Martins Silverio Cardoso
#04/10/2017

#importa as funcoes para manipular XML
from xml.dom.minidom import parse, parseString

arquivo = parse('teste//xml//t1.xml') #abre o arquivo XML
grade = open('teste//gradeDeEntidade//t1.txt','w')

sentencas = arquivo.getElementsByTagName('s') # Recupera todas as sentencas que existem no arquivo

print len(sentencas)# imprime o tamanho da lista ( ou seja quantidade de sentencas)

w= 'teste'

p = {}
p['palavras'] = '--'
p['avião'] = '123'
p['p2'] = 'x'
p[w] = 'deu certo'
print p['palavras']
w = 'n2'
p[w] = 'outravez'
print p['p2']
pp = {}
pp['pq'] = p
p['p2'] = p['p2']+'--'

print p['p2']
print pp



palavras = {}
for i in range(len(sentencas)): 
    print "esse e o i", i
    terminais = sentencas[i].getElementsByTagName('t')
    naoterminais = sentencas[i].getElementsByTagName('nt')
    print 'tamanho terminais = ', len(terminais)
    print 'tamanho naoterminais = ', len(naoterminais)
    

    for nterminal in naoterminais:
        if str(nterminal.attributes['cat'].value) != 'pp':
            linhas = nterminal.getElementsByTagName('edge')
            
            for l in linhas:
                att = l.attributes['label'].value
                if att == 'Od' or att == 'S' or att == 'H':
                    idref = l.attributes['idref'].value
                    idint = int(idref[3:])-1
                    if idint <= len(terminais)+1:
                        classe = terminais[idint].attributes['pos'].value
                        #classegrid = '--'
                        if classe == 'n':
                               classegrid = 'S'
                        elif classe =='Od':
                               classegrid ='O'
                        else:
                               classegrid='X'
                        print '===================================================='
                        print 'valor do idint', idint
                        print terminais[idint].attributes['word'].value
                        print '++++++++++++++++++++++++++++++++++++++++++++++++++++'
                        #ident = str(terminais[idint].attributes['word'].value)
                        ident = terminais[idint].attributes['word'].value
                        if ident in palavras:
                            palavras[ident] += classegrid
                        else:
                            palavras[ident] = classegrid
                        for pl in palavras:
                            print 'teste de pl', len(palavras[pl])
                            if len(palavras[pl]) == i:
                                palavras[pl] += '-'
                            elif len(palavras[pl]) < i+1:
                                palavras[pl] = ('-'*i) + palavras[pl]
                                
print palavras
gradecpl =''
for pl in palavras:
    gradecpl += ' %30s  %s\n' % (pl,palavras[pl])
print gradecpl
               
grade.write(gradecpl.encode(encoding='UTF-8',errors='strict'))
grade.close()
#for senteca in sentencas
    

print 'ok'# para debug


