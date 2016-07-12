# -*- coding: UTF-8 -*-

while True:
	d, n = raw_input().split()
	if(int(d) == 0 and int(n) == 0):
		break
	new = n.replace(d, "")
	if (new == ""):
		print 0
	else:
		print abs(int(new))