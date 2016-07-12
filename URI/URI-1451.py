# -*- coding: utf-8 -*-

while True:
	try:
		entrada = raw_input()
		palavra = ''
		aux = ''
		cursor = 0 #0 para home, 1 para end
		for i in entrada:
			if(i == '['):
				if(cursor == 0):
					palavra = aux + palavra
				else:
					palavra += aux
				aux = ''
				cursor = 0
			elif(i == ']'):
				if(cursor == 0):
					palavra = aux + palavra
				else:
					palavra += aux
				aux = ''
				cursor = 1
			else:
				aux += i
		if(cursor == 0):
			palavra = aux + palavra
		else:
			palavra += aux
			aux = ''
			
		print palavra
	except EOFError:
		break