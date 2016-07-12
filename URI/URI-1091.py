# -*- coding: utf-8 -*-

while True:
	qtd_casa = int(raw_input())
	if(qtd_casa == 0):
		break
	x_ponto, y_ponto = map(int, raw_input().split())
	for i in range(qtd_casa):
		x_casa, y_casa = map(int, raw_input().split())
		if(x_casa > x_ponto and y_casa > y_ponto):
			print "NE"
		elif(x_casa > x_ponto and y_casa < y_ponto):
			print "SE"
		elif(x_casa < x_ponto and y_casa > y_ponto):
			print "NO"
		elif(x_casa < x_ponto and y_casa < y_ponto):
			print "SO"
		else:
			print "divisa"
