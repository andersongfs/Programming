# -*- coding: utf-8 -*-

a = raw_input()
b = raw_input()
yay = 0
whoops = 0
dicio = {}
noYay = []

for letter in b:
	if dicio.has_key(letter):
		dicio[letter] += 1
	else:
		dicio[letter] = 1

for l in a:
	if dicio.has_key(l) and dicio[l] >= 1:
		dicio[l] -= 1
		yay += 1
	else:
		noYay.append(l)	

for l in noYay:
	if dicio.has_key(l.swapcase()) and dicio[l.swapcase()] >= 1:
		dicio[l.swapcase()] -= 1
		whoops += 1
			
print yay, whoops

