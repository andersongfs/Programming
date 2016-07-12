# -*- coding: utf-8 -*-

while True:
	try:
		grau = int(raw_input())
		print "Y" if(grau % 6 == 0) else "N"
	except EOFError:
		break
