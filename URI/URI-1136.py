# -*- coding: utf-8 -*-

def resultado(numPossiveis):
	for i in numNecessarios:
		if i == False:
			return "N"
	return "Y"

while True:
	n, b = map(int, raw_input().split())
	if n == 0 and b == 0:
		break

	bolas = map(int, raw_input().split(" "))
	numNecessarios = [False]*(n+1)

	for i in range(len(bolas)):
		for j in range(i, len(bolas)):
			diferenca = abs(bolas[i] - bolas[j])
			if  diferenca <= len(numNecessarios):
				numNecessarios[diferenca] = True

	print resultado(numNecessarios)


