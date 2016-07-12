# -*- coding: utf-8 -*-
import math
#lucas exponencial e pedro fatorial
lucas = 0 # lucas eh 0
pedro = 0 # pedro eh 1
rodadas = []
qtd_entrada = int(raw_input())
for i in range(qtd_entrada):
	a, b = map(int, raw_input().split('^'))
	n = int(raw_input()[:-1])
	exp = b * math.log10(a)
	fat = 0
	for f in range(1, n + 1):
		fat += math.log10(f)
	if(exp >= fat):
		rodadas.append(0)	
		lucas += 1
	else:
		rodadas.append(1)
		pedro += 1

if(pedro == lucas):
	print 'A competicao terminou empatada!'
elif(pedro > lucas):
	print 'Campeao: %s!' %('Pedro')
else:
	print 'Campeao: %s!' %('Lucas')

for i in range(len(rodadas)):
	if(rodadas[i] == 0):
		print 'Rodada #%d: Lucas foi o vencedor' %(i+1)
	else:
		print 'Rodada #%d: Pedro foi o vencedor' %(i+1)
