# -*- coding: utf-8 -*-

braille = "B"
decimal = "S"
braToDec = {".***" : 0,"*..." : 1, "*.*." : 2, "**.." : 3, "**.*" : 4, 
				"*..*" : 5, "***." : 6, "****" : 7, "*.**" : 8, ".**." : 9}
decToBra = {0 : ".***..", 1 : "*.....",  2 : "*.*...",  3 : "**....", 4 : "**.*..", 
				5 : "*..*..", 6 : "***...", 7 : "****..", 8 : "*.**..", 9 : ".**..."}

def convertEmDec(tamEntrada):
	resultado = ""
	linha1 = raw_input().split(" ")
	linha2 = raw_input().split(" ")
	linha3 = raw_input().split(" ")
	for i in range(tamEntrada):
		resultado += str(braToDec[linha1[i]+linha2[i]])

	return resultado

def convertEmBraille(tamEntrada):
	linha1 = []
	linha2 = []
	linha3 = []
	entrada = raw_input()
	for i in entrada:
		convertido = decToBra[int(i)]
		linha1.append(convertido[0:2])
		linha2.append(convertido[2:4])
		linha3.append(convertido[4:6])
	for i in range(tamEntrada):
		print linha1[i],
	print
	for i in range(tamEntrada):
		print linha2[i],
	print
	for i in range(tamEntrada):
		print linha3[i],
	print


while True:
	qtdDaEntrada = int(raw_input())
	if qtdDaEntrada == 0:
		break

	tipoDaEntrada = raw_input()
	if tipoDaEntrada == braille:
		print convertEmDec(qtdDaEntrada)
	elif tipoDaEntrada == decimal:
		convertEmBraille(qtdDaEntrada)