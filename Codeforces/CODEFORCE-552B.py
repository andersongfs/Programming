entrada = raw_input()

soma = 0
tamanho = len(entrada)
if(tamanho == 1):
	print entrada
else:
	a = int(entrada)
	b = (10**(tamanho - 1)) - 1
	c = (a - b) * tamanho
	soma += c
	for i in range(0, tamanho-1):
		soma += (9 * 10**i) * (i+1)


	print soma