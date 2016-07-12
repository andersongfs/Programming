# -*- codingo: utf-8 -*-
INSERIR = 1
REMOVER = 2
while True:
	ehpilha = True
	ehfila = True
	ehprioridade = True
	s = []
	q = []
	pq = []

	try:
		qtd = int(raw_input())
		for i in range(qtd):
			op, num = map(int, raw_input().split())
			if(op == INSERIR):
				s.append(num)
				q.append(num)
				pq.append(num)
			elif(op == REMOVER):
				if(not ehpilha and not ehfila and not ehprioridade):
					break	
				elif(not ehpilha and not ehfila and ehprioridade):
					pq.sort()
					pqremovido = pq.pop()
					if(pqremovido != num):
						ehprioridade = False

				elif(not ehpilha and  ehfila and not ehprioridade):
					qremovido = q.pop(0)
					if(qremovido != num):
						ehfila = False

				elif(not ehpilha and  ehfila and  ehprioridade):
					qremovido = q.pop(0)
					if(qremovido != num):
						ehfila = False

					pq.sort()
					pqremovido = pq.pop()
					if(pqremovido != num):
						ehprioridade = False	

				elif( ehpilha and not ehfila and not ehprioridade):
					sremovido = s.pop()
					if(sremovido != num):
						ehpilha = False

				elif( ehpilha and not ehfila and  ehprioridade):
					sremovido = s.pop()
					if(sremovido != num):
						ehpilha = False

					pq.sort()
					pqremovido = pq.pop()
					if(pqremovido != num):
						ehprioridade = False

				elif( ehpilha and  ehfila and not ehprioridade):
					sremovido = s.pop()
					if(sremovido != num):
						ehpilha = False

					qremovido = q.pop(0)
					if(qremovido != num):
						ehfila = False

				elif( ehpilha and  ehfila and  ehprioridade):
					sremovido = s.pop()
					if(sremovido != num):
						ehpilha = False

					qremovido = q.pop(0)
					if(qremovido != num):
						ehfila = False

					pq.sort()
					pqremovido = pq.pop()
					if(pqremovido != num):
						ehprioridade = False

		q = 1 if ehfila else 0
		s = 1 if ehpilha else 0
		pq = 1 if ehprioridade else 0


		if((ehprioridade + ehfila + ehpilha) > 1):
			print "not sure"
		elif((ehprioridade + ehfila + ehpilha) == 0):
			print "impossible"
		else:
			if(ehfila):
				print "queue"
			elif(ehpilha):
				print "stack"
			elif(ehprioridade):
				print "priority queue"
	

	except EOFError:
		break