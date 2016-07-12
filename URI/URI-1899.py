# https://www.urionlinejudge.com.br/judge/pt/problems/view/1899
# -*- coding: utf-8 -*-
 
qtd_paredes = int(raw_input())
coeficientes_possiveis = []
coefAngA, coefAngB = 0, 0
 
for i in range(qtd_paredes+1):
	d, a1, a2 = map(int, raw_input().split())
	coefAngA = (float(a1))/d
	coefAngB = (float(a2))/d
	coeficientes_possiveis.append([coefAngA, coefAngB])
 
possivel = True
for i in range(1, len(coeficientes_possiveis)):
	if (coeficientes_possiveis[i][0] > coeficientes_possiveis[i-1][1]) or (coeficientes_possiveis[i][1] < coeficientes_possiveis[i-1][0]):
		possivel = False
		break
	else:
		if (coeficientes_possiveis[i][0] < coeficientes_possiveis[i-1][0]):
			coeficientes_possiveis[i][0] = coeficientes_possiveis[i-1][0]
		if (coeficientes_possiveis[i][1] > coeficientes_possiveis[i-1][1]):
			coeficientes_possiveis[i][1] = coeficientes_possiveis[i-1][1]
 
if possivel:
	print "Y"
else:
	print "N"