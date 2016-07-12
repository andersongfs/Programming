# -*- coding: utf-8 -*-

def populateC():
    c.append(b[-1])
    for i in b:
        c.append(i)
    c.append(b[0])
while True:
	a = int(raw_input())
	if(a == 0):
		break
	b = map(int, raw_input().split())
	c = []
	counter = 0
	populateC()
	for i in range(1, ((len(c))-1)):
	    if((c[i] < c[i-1] and c[i] < c[i+1]) or (c[i] > c[i-1] and c[i] > c[i+1])):
	        counter += 1

	print counter