# -*- coding: utf-8 -*-
mortos = set()
assassinos = {}
while True:
	try:
		a, m = raw_input().split()
		if(a in assassinos):
			assassinos[a] += 1
		else:
			assassinos[a] = 1
		mortos.add(m)
	except EOFError:
		break

ordem = assassinos.keys()
ordem.sort()
print 'HALL OF MURDERERS'
for i in ordem:
	if(i not in mortos):
		print i, assassinos[i]
