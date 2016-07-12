
entrada = raw_input()
while(entrada != -1):
	if(len(entrada) > 2): 
		if( entrada[1] == 'x'):
			print int(entrada, 16)
	else:
		print '0x', hex(entrada.split('x')[1])

	entrada = raw_input()