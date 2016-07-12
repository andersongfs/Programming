# -*- coding: utf-8 -*-

qtd_cidades = input()
cidades = map(int, raw_input().split(" "))
for i in range(len(cidades)):
	menor = 0
	maior = 0
	if i == 0:
		menor = abs(cidades[0] - cidades[1])
		maior = abs(cidades[0] - cidades[-1])
	if i == qtd_cidades - 1:
		menor = abs(cidades[i] - cidades[i-1])
		maior = abs(cidades[i] - cidades[0])
	else:
		menor = min( abs((cidades[i]) - (cidades[i-1])), abs((cidades[i]) - (cidades[i+1])) )
		maior = max( abs((cidades[i]) - (cidades[0])), abs((cidades[i]) - (cidades[-1])) )

	print menor, maior

