# -*- coding: utf-8 -*-
ordem = ["branco P", "branco M", "branco G", "vermelho P", "vermelho M", "vermelho G"]
qtd_entrada = int(raw_input())

while(qtd_entrada != 0):
	dic = {"branco P" : [], "branco M" : [], "branco G" : [], "vermelho P" : [], "vermelho M" : [], "vermelho G" : []}
	for i in range(qtd_entrada):
		nome = raw_input()
		camisa = raw_input()
		dic[camisa].append(nome)
	for i in ordem:
		atual = dic[i]
		atual.sort()
		for j in atual:
			print i, j

	qtd_entrada = int(raw_input())
	if(qtd_entrada != 0):
		print