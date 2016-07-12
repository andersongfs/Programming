# -*- coding: utf-8 -*-

qtdTestes = int(raw_input())

for i in range(qtdTestes):
	entrada = raw_input()
	abre = 0
	fecha = 0
	diamantes = 0
	for j in entrada:
		if(abre > 0 and j == ">"):
			abre -= 1
			diamantes += 1
		if(j == "<"):
			abre += 1
	print diamantes