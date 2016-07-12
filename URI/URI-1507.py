# -*- coding: utf-8 -*-
def eh_subseq(palavra, frase):
	index = 0
	for i in palavra:
		posicao_encontrada = frase.find(i, index, len(frase))
		if(posicao_encontrada != -1): # o find retorna -1 caso nao encontre
			index = posicao_encontrada + 1 # +1 para que comece a buscar na posicao depois da que ja foi encontrado
		else:
			return False
	return True


qtd_testes = int(raw_input())

for i in range(qtd_testes):
	frase = raw_input()
	qtd_buscas = int(raw_input())
	for j in range(qtd_buscas):
		palavra = raw_input()
		if(eh_subseq(palavra, frase)):
			print "Yes"
		else:
			print "No"