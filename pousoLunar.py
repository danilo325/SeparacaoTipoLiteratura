#Jogo alunisagem (pousoLunar)
#pousoLunar.py

#importa funcao sqrt do modulo math

from math import sqrt

x=500. #altitude em pes
v = -50. #velocidade em pes/s
g = -5. #aceleracao em pes/s^2
t = 1. #tempo entre jogadas em segundos
comb = 120 #quantidade de combustivel

print "Simulacao de alunisagem"
print
print '(digite a quantidade de combustivel a queimar)'

fmt = 'Alt: %6.2f Vel: %6.2f Comb: %3d'
while x > 0: #enquanto nao toca o solo
	msg = fmt % (x, v, comb)
	if comb > 0:
		resp = raw_input(msg + ' Queima = ')
		try:
			queima = float(resp)
		except:
			queima = 0;
		if queima > comb:
			queima = comb
		comb = comb - queima
		a = g + queima
	else:
		print msg
		a =g
	x0 = x
	v0 = v
	x = x0 + v0*t + a*t*t/2
	v = v0 + a*t
	
vf = sqrt(v0*v0 + 2*-a*x0)
print '>>> Contato! Velociadade final: %6.2f' % (-vf)

if vf == 0:
	msg = 'Alunisagem perfeita'
elif vf <= 2:
	msg = ' Alunisagem dentro do padrao'
elif vf <= 10:
	msg = 'Alunisagem com avarias leves'
elif vf <= 20:
	msg = 'Alunisagem com avarias severas'
else:
	msg = 'Modulo lunar destruido no impacto'

print '>>>>'+msg
