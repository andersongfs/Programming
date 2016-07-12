# -*- coding: utf-8 -*-

def foiAtingido(altura, movimento):
	parado = "S"
	pulo = "J"
	if altura <= 2 and movimento == parado:
		return True
	elif altura > 2 and movimento == pulo:
		return True
	else:
		return False

qtdDeTestes = int(raw_input())
for i in range(qtdDeTestes):
	qtdTiros = int(raw_input())
	tiros = map(int, raw_input().split(" "))
	movimentos = raw_input().split(" ")

	qtdAtingido = 0
	for j in range(qtdTiros):
		if foiAtingido(tiros[j], movimentos[0][j]):
			qtdAtingido += 1

	print qtdAtingido




