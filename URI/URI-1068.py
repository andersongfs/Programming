# -*- coding: utf-8 -*-

while True:
	try:
		entrada = raw_input()
		num = 0
		for i in entrada:
			if(i == "("):
				num = num + 1
			elif(i == ")"):
				if(num == 0):
					num = num - 1
					break
				num = num - 1
		if (num == 0):
			print "correct"
		else:
			print "incorrect"

	except EOFError:
		break