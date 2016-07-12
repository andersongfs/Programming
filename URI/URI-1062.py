# -*- coding: utf-8 -*-

num_vagoes = int(raw_input())
while num_vagoes != 0:
	vagoes = map(int, raw_input().split())
	pilha = []
	vagaoDaVez = num_vagoes
	saida = []
	if(vagoes[0] == 0):
		num_vagoes = int(raw_input())
		print
		continue

	for k in range(num_vagoes):
		i = vagoes.pop()
		if(len(pilha) == 0):
			if(i == vagaoDaVez):
				vagaoDaVez -= 1
				continue
			else:
				pilha.append(i)
		else:
			if(i == vagaoDaVez):
				vagaoDaVez -= 1
				
				while(pilha[-1] == vagaoDaVez):
					pilha.pop()
					vagaoDaVez -= 1
					if(len(pilha) == 0): break
			else:
				while(pilha[-1] == vagaoDaVez):
					pilha.pop()
					vagaoDaVez -= 1
					if(len(pilha) == 0): break

				pilha.append(i)

				while(pilha[-1] == vagaoDaVez):
					pilha.pop()
					vagaoDaVez -= 1
					if(len(pilha) == 0): break

	if(len(pilha) > 0):
		print "No"
	else:
		print "Yes"

