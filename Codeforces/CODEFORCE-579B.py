#http://codeforces.com/problemset/problem/579/B

n = int(raw_input())
lista_de_forca = []
dic = {}

for k in range(2, 2*n + 1):
	forcas = map(int, raw_input().split())
	for s in range(len(forcas)):
		lista_de_forca.append(forcas[s])
		dic[forcas[s]] = [k, s + 1]

lista_de_forca.sort(reverse=True)
contador = 0
usados = [0] * 2*n

for i in lista_de_forca:
	posicao = dic[i]
	if(posicao[0] not in usados) and (posicao[1] not in usados):
		usados[(posicao[1])-1] = posicao[0]
		usados[(posicao[0])-1] = posicao[1]
		contador += 1
	if(contador == n): break


print ' '.join(map(str, usados))
