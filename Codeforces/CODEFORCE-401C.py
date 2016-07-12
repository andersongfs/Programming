zeros, uns = map(int, raw_input().split())
r = ''
ultimo_inserido = -1
exp1 = (uns <= (2*zeros + 2))
exp2 = (uns >= (zeros -1))		
if(not (exp1 and exp2)):
	r += '-1'
	zeros = 0
	uns = 0

while(zeros>0 or uns>0):
	if(ultimo_inserido != 0):
		
		if(zeros >= uns):
			r += '0'
			zeros -= 1
			ultimo_inserido = 0
		elif(ultimo_inserido == 1):
			r += '0'
			zeros -= 1
			ultimo_inserido = 0

	if(ultimo_inserido != 1):
		if(uns <= zeros and uns > 0):
			r += '1'
			uns -= 1
			ultimo_inserido = 1
		elif(uns == 1):
			r += '1'
			uns -= 1
			ultimo_inserido = 1
		elif(uns > 1):
			r += '11'
			uns -= 2
			ultimo_inserido = 1


print r