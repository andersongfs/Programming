# -*- coding: utf-8 -*- 

qtd_entrada = int(raw_input())
TOTAL_CONSOANTES = 26
TOTAL_DIGITOS = 10
for i in range(qtd_entrada):
	c, d = map(int, raw_input().split())
	if(c == 0 and d == 0):
		print 0
	elif(c == 0 and d != 0):
		print TOTAL_DIGITOS ** d
	elif(c != 0 and d == 0):
		print TOTAL_CONSOANTES ** c 
	else:
		print (TOTAL_CONSOANTES ** c) * (TOTAL_DIGITOS ** d)
