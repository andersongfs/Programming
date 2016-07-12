# -*- coding: utf-8 -*-

while True:
	try:	
		num1, num2 = raw_input().split(' ')
		num1 = int(num1)
		num2 = int(num2)
		sem_repeticoes = 0
		while num1 <= num2:
			if len(str(num1)) == len(set(str(num1))):
				sem_repeticoes += 1

			num1 += 1
		print sem_repeticoes
	except EOFError:
		break
