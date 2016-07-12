# -*- coding: utf-8 -*-

a = raw_input()
b = raw_input()
cpf = "" 
line1 = ""
line2 = ""

def extractNum(str):
	for i in range(len(str)):
		if(str[i] == "."):
			if(len(str) >= i+2):
				return str[:i+3]
			elif(len(str) == i+1):
				return str[:i+2]
			else:
				return str[:i]
	return str

for i in a:
	if (i.isdigit() or i == "."):
		line1 += i

for i in b:
	if (i.isdigit() or i == "."):
		line2 += i

print "cpf " + line1[:11]
value = float(extractNum(line1[11:])) + float(extractNum(line2))
print "%.2f" %value
